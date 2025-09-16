import streamlit as st
from pathlib import Path
import sys
import os
import json
from dotenv import load_dotenv

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.chatbot2.chatbot import Chatbot
from src.chatbot2.session import ChatSession
from src.pdf2txt import extract_text_from_pdf

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="Hashbrown Chatbot", layout="wide")

# Initialize session state
if "chat_session" not in st.session_state:
    st.session_state.chat_session = ChatSession()

# Initialize chatbot
if "chatbot" not in st.session_state:
    try:
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY in .env")

        st.session_state.chatbot = Chatbot(openai_api_key=openai_api_key)
    except Exception as e:
        st.error(f"Failed to initialize chatbot: {e}")
        st.stop()

# --- Main App ---
st.title("HASHBROWN")

# Two-column layout
col1, col2 = st.columns([2, 1])

with col1:
    # Input section
    st.subheader("Client Information")

    # File upload
    uploaded_file = st.file_uploader("Upload PDF/TXT", type=["pdf", "txt"])

    # Text input
    client_text = st.text_area(
        "Describe the client:",
        height=100,
        placeholder="Example: We have a sight LC and need financing...",
    )

    # Process button
    if st.button("Analyze", type="primary"):
        chatbot = st.session_state.chatbot
        session = st.session_state.chat_session

        # Extract text from file if uploaded
        uploaded_text = ""
        if uploaded_file:
            if uploaded_file.type == "application/pdf":
                uploaded_text = extract_text_from_pdf(uploaded_file)
            else:
                uploaded_text = uploaded_file.read().decode("utf-8")

        # Combine texts
        full_text = "\n".join(filter(None, [uploaded_text, client_text]))

        if full_text.strip():
            # Process with LLM if input is provided
            with st.spinner("Processing..."):
                try:
                    client_info = chatbot.process_client_input(full_text, session)

                    if session.role_determined:
                        role_str = []
                        if session.is_seller:
                            role_str.append("Seller")
                        if session.is_buyer:
                            role_str.append("Buyer")
                        st.success(
                            f"Analysis complete! Client role: {' & '.join(role_str) if role_str else 'Unknown'}"
                        )
                    else:
                        st.info("Text processed. Please confirm your role below.")

                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            # No input provided - set up empty facts for manual navigation
            session.facts = {}
            session.client_information = {}
            session.products = []
            session.initial_processing_done = True
            # Note: Tree will be loaded after role is determined
            st.info("No preanswered nodes - role clarification required")

    # Reset button
    if st.button("Reset"):
        st.session_state.chat_session = ChatSession()
        st.rerun()

    # Current question section
    session = st.session_state.chat_session

    # Handle role clarification if needed (when role is completely unknown)
    if (
        session.initial_processing_done
        and not session.role_determined
        and not session.is_seller
        and not session.is_buyer
    ):
        chatbot = st.session_state.chatbot
        role_question = chatbot.get_role_clarification_question(session)

        st.subheader("Role Clarification")
        st.write(role_question["question"])

        # Role selection buttons
        for i, option in enumerate(role_question["options"]):
            if st.button(option["text"], key=f"role_{i}"):
                success = chatbot.process_role_response(session, option["value"])
                if success:
                    st.rerun()
                else:
                    st.error("Error processing role selection")

    # Normal decision tree questions
    elif session.initial_processing_done and session.role_determined:
        chatbot = st.session_state.chatbot
        next_question = chatbot.get_next_question(session)

        if next_question:
            if next_question["type"] == "question":
                st.subheader("Question")
                st.write(next_question["question"])

                # Answer buttons
                for i, option in enumerate(next_question["options"]):
                    if st.button(option["text"], key=f"ans_{i}"):
                        chatbot.process_user_response(
                            session, option["value"], option["target"]
                        )
                        st.rerun()

            elif next_question["type"] == "end":
                st.subheader("🎯 Recommendation Complete")

                # Show list of products discovered during traversal
                facts_data = session.to_json()
                products = facts_data.get("products", [])

                if products:
                    st.write("**Recommended Products:**")
                    for i, product in enumerate(products, 1):
                        # Clean product name (remove any attr metadata if present)
                        clean_product = (
                            product.split(" | attr=")[0]
                            if " | attr=" in product
                            else product
                        )
                        st.success(f"**{i}. {clean_product}**")
                else:
                    st.info("No specific products recommended based on your inputs.")

with col2:
    # Facts JSON section
    st.subheader("Facts JSON")

    session = st.session_state.chat_session
    # Use the complete enhanced facts JSON from session
    facts_data = session.to_json()

    # Extract and remove original_input from client_information
    original_input = None
    if (
        "client_information" in facts_data
        and "original_input" in facts_data["client_information"]
    ):
        original_input = facts_data["client_information"].pop("original_input")

    # Display as formatted JSON
    st.code(json.dumps(facts_data, indent=2), language="json")

    # Show original input separately if it exists
    if original_input:
        st.subheader("Original Input")
        st.text_area("", value=original_input, disabled=True, height=100)
