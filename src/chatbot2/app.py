import streamlit as st
from pathlib import Path
import sys
import os
from dotenv import load_dotenv

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.chatbot2.chatbot import Chatbot
from src.chatbot2.session import ChatSession
from src.pdf2txt import extract_text_from_pdf
from src.chatbot2.models import SellerPostShipmentLCDecision

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="Client Chatbot", layout="wide")

# Initialize session state
if "conversation_stage" not in st.session_state:
    st.session_state.conversation_stage = (
        "initial"  # "initial", "chatting", "completed"
    )
if "chat_session" not in st.session_state:
    st.session_state.chat_session = ChatSession()

# --- Decision tree info ---
TREE_MD_PATH = "src/decision_trees/seller_post_shipment.md"
TREE_NAME = "SellerPostShipmentLC"
TREE_CONTEXT = "Decision tree for Seller Post-shipment LC Payment"

# --- Initialize chatbot once ---
if "chatbot" not in st.session_state:
    try:
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError("OpenAI API key is required. Set OPENAI_API_KEY in .env")

        st.session_state.chatbot = Chatbot(
            openai_api_key=openai_api_key,
            tree_md_path=TREE_MD_PATH,
            tree_name=TREE_NAME,
            tree_context=TREE_CONTEXT,
        )
        st.session_state.openai_api_key = openai_api_key
    except Exception as e:
        st.error(f"Failed to initialize chatbot: {e}")
        st.stop()


def display_initial_form():
    """Display the initial form for document/text input."""
    st.title("🏦 Client Chatbot")

    st.subheader("📄 Share Information About Your Client")
    st.markdown("Please provide information about your client:")

    # File upload
    uploaded_file = st.file_uploader(
        "Upload a PDF or TXT file with your trade details",
        type=["pdf", "txt"],
        help="Upload documents containing your trade finance requirements",
    )

    # Text input
    client_text_input = st.text_area(
        "Or describe your trade finance needs here:",
        placeholder="Example: My Client is an importer of electronics.",
        height=150,
    )

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        process_button = st.button(
            "🚀 Start Analysis", type="primary", use_container_width=True
        )

    if process_button:
        chatbot: Chatbot = st.session_state.chatbot

        # Extract text from uploaded file if any
        uploaded_text = ""
        if uploaded_file:
            with st.spinner("Processing uploaded file..."):
                if uploaded_file.type == "application/pdf":
                    uploaded_text = extract_text_from_pdf(uploaded_file)
                elif uploaded_file.type == "text/plain":
                    uploaded_text = uploaded_file.read().decode("utf-8")

        # Combine uploaded text and manual input
        full_client_text = "\n".join(filter(None, [uploaded_text, client_text_input]))

        if not full_client_text.strip():
            st.error("Please provide client input text or upload a file.")
            return

        # Process input
        with st.spinner("Analyzing your requirements..."):
            try:
                result: SellerPostShipmentLCDecision = chatbot.process_client_input(
                    full_client_text, st.session_state.chat_session
                )

                st.session_state.conversation_stage = "chatting"
                st.rerun()

            except Exception as e:
                st.error(f"Error processing your input: {e}")


def display_conversation():
    """Display the interactive conversation interface."""
    st.title("💬 Product Recommendation Chat")

    chatbot: Chatbot = st.session_state.chatbot
    session: ChatSession = st.session_state.chat_session

    # Display conversation history
    if session.conversation_history:
        st.subheader("📋 Conversation History")
        for i, turn in enumerate(session.conversation_history):
            with st.expander(f"Q{i+1}: {turn['question'][:50]}..."):
                st.markdown(f"**Question:** {turn['question']}")
                st.markdown(f"**Your Answer:** {turn['answer']}")

    # Get next question or end state
    next_question = chatbot.get_next_question(session)

    if not next_question:
        st.error("Something went wrong. Unable to continue conversation.")
        if st.button("🔄 Restart"):
            st.session_state.conversation_stage = "initial"
            st.session_state.chat_session = ChatSession()
            st.rerun()
        return

    if next_question["type"] == "end":
        display_final_recommendation(next_question)
        return

    # Display current question
    st.subheader("❓ Current Question")
    st.markdown(f"**{next_question['question']}**")

    # Display response options as buttons
    st.markdown("Please select your answer:")

    cols = st.columns(len(next_question["options"]))
    for i, option in enumerate(next_question["options"]):
        with cols[i]:
            if st.button(
                option["text"],
                key=f"option_{i}",
                use_container_width=True,
                type="secondary",
            ):
                # Process the user's response
                success = chatbot.process_user_response(
                    session, option["value"], option["target"]
                )

                if success:
                    st.rerun()
                else:
                    st.error("Error processing your response. Please try again.")

    # Show debug info in expander
    with st.expander("🔧 Debug Info"):
        st.json(
            {
                "current_node": session.current_node_id,
                "facts": session.facts,
                "conversation_turns": len(session.conversation_history),
            }
        )


def display_final_recommendation(end_info):
    """Display the final recommendation."""
    st.subheader("🎯 Final Recommendation")

    session: ChatSession = st.session_state.chat_session

    # Map node IDs to product recommendations
    product_recommendations = {
        "G": {
            "title": "Export Bill under Letter of Credit",
            "description": "Perfect for your Sight LC transaction with financing needs",
            "benefits": [
                "Immediate cash flow through bill discounting",
                "Risk mitigation with LC backing",
                "Faster access to funds before buyer payment",
            ],
            "icon": "💳",
        },
        "H": {
            "title": "Wait for Sight Payment",
            "description": "Best option for your Sight LC without financing needs",
            "benefits": [
                "No additional costs or fees",
                "Simple and straightforward process",
                "Full payment upon document presentation",
            ],
            "icon": "⏳",
        },
        "I": {
            "title": "Bill Receivable under Letter of Credit",
            "description": "Ideal for your Usance LC transaction with financing needs",
            "benefits": [
                "Bridge financing until LC maturity",
                "Enhanced cash flow management",
                "Risk coverage through LC guarantee",
            ],
            "icon": "📋",
        },
        "J": {
            "title": "Wait for Usance Payment",
            "description": "Suitable for your Usance LC without immediate financing needs",
            "benefits": [
                "No additional financing costs",
                "Payment guaranteed at maturity",
                "Standard trade finance process",
            ],
            "icon": "📅",
        },
    }

    recommendation = product_recommendations.get(
        end_info["node_id"],
        {
            "title": f"Product Recommendation ({end_info['node_id']})",
            "description": "Based on your requirements",
            "benefits": ["Tailored to your specific needs"],
            "icon": "🎯",
        },
    )

    # Display recommendation card
    st.markdown(f"### {recommendation['icon']} {recommendation['title']}")
    st.info(recommendation["description"])

    st.markdown("**Key Benefits:**")
    for benefit in recommendation["benefits"]:
        st.markdown(f"• {benefit}")

    # Display path taken
    st.subheader("📊 Decision Path")
    if session.conversation_history:
        for i, turn in enumerate(session.conversation_history):
            st.markdown(f"**{i+1}.** {turn['question']}")
            st.markdown(f"   → *{turn['answer']}*")

    # Action buttons
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("🔄 Start New Consultation", type="primary"):
            st.session_state.conversation_stage = "initial"
            st.session_state.chat_session = ChatSession()
            st.rerun()

    with col2:
        if st.button("📋 View Details", type="secondary"):
            st.session_state.conversation_stage = "completed"
            st.rerun()


def display_detailed_results():
    """Display detailed results and analysis."""
    st.title("📊 Detailed Analysis")

    session: ChatSession = st.session_state.chat_session

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎯 Final Recommendation")
        # Show the same recommendation as before
        # (implementation would be similar to display_final_recommendation)

    with col2:
        st.subheader("📈 Analysis Summary")
        st.json(session.to_json(), expanded=True)

    if st.button("🔄 Start New Consultation"):
        st.session_state.conversation_stage = "initial"
        st.session_state.chat_session = ChatSession()
        st.rerun()


# --- Main App Logic ---
if "chatbot" in st.session_state:
    if st.session_state.conversation_stage == "initial":
        display_initial_form()
    elif st.session_state.conversation_stage == "chatting":
        display_conversation()
    elif st.session_state.conversation_stage == "completed":
        display_detailed_results()
