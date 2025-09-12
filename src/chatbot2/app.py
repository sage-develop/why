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

        st.session_state.chatbot = Chatbot(
            openai_api_key=openai_api_key,
            tree_md_path="src/decision_trees/seller_post_shipment.md",  # TODO: Load in multiple trees
            tree_name="SellerPostShipmentLC",
            tree_context="Decision tree for Seller Post-shipment LC Payment",
        )
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
        "Describe your trade finance needs:",
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
                    chatbot.process_client_input(full_text, session)
                    st.success("Analysis complete!")
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            # No input provided - set up empty facts for manual navigation
            session.facts = {}  # Empty facts JSON
            session.initial_processing_done = True

            # Set starting node manually (first decision node)
            all_nodes = chatbot._get_all_nodes()
            from src.chatbot2.models import NodeType

            first_decision_node = next(
                (node for node in all_nodes if node.node_type == NodeType.DECISION),
                None,
            )
            session.current_node_id = (
                first_decision_node.node_id if first_decision_node else None
            )

            st.info("No preanswered nodes")

    # Reset button
    if st.button("Reset"):
        st.session_state.chat_session = ChatSession()
        st.rerun()

    # Current question section
    session = st.session_state.chat_session
    if session.initial_processing_done:
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
                st.subheader("Recommendation")
                # Get product name directly from the node
                chatbot = st.session_state.chatbot
                end_node = chatbot.find_node_by_id(next_question["node_id"])

                if end_node and end_node.question:
                    product_name = end_node.question.strip()
                else:
                    product_name = f"Product {next_question['node_id']}"

                st.success(f"**{product_name}**")

                # Show conversation path
                if session.conversation_history:
                    st.write("**Decision Path:**")
                    for i, turn in enumerate(session.conversation_history):
                        st.write(f"{i+1}. {turn['question']}")
                        st.write(f"   → {turn['answer']}")

with col2:
    # Facts JSON section
    st.subheader("Facts JSON")

    session = st.session_state.chat_session
    facts_data = {
        "current_node": session.current_node_id,
        "facts": session.facts,
        "conversation_turns": len(session.conversation_history),
    }

    # Display as formatted JSON
    st.code(json.dumps(facts_data, indent=2), language="json")
