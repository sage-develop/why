import streamlit as st
from dotenv import load_dotenv
from pathlib import Path
import sys
import os

# Add the project root to the Python path
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from src.chatbot.chatbot import GlobalMarketsChatbot

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(page_title="Global Markets Product Chatbot", layout="wide")

# Initialize chatbot
if "chatbot" not in st.session_state:
    try:
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            raise ValueError(
                "OpenAI API key is required. Set OPENAI_API_KEY environment variable."
            )
        st.session_state.chatbot = GlobalMarketsChatbot(openai_api_key)
        st.session_state.openai_api_key = openai_api_key
        st.session_state.initialized = True
    except Exception as e:
        st.session_state.initialized = False
        st.session_state.init_error = str(e)

if "current_session" not in st.session_state:
    st.session_state.current_session = None

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# Header
st.title("Global Markets Product Chatbot")
st.markdown("---")

# Initialization error check
if not st.session_state.get("initialized", False):
    st.error("**Failed to Initialize Chatbot**")
    st.error(f"Error: {st.session_state.get('init_error', 'Unknown error')}")
    st.stop()

# Sidebar
with st.sidebar:
    st.header("Menu")

    if st.button("🆕 Start New Consultation", type="primary"):
        try:
            response, session = st.session_state.chatbot.start_consultation()
            st.session_state.current_session = session
            st.session_state.conversation_history = [
                {"type": "bot", "content": response}
            ]
            st.rerun()
        except Exception as e:
            st.error(f"Error starting consultation: {e}")

    if st.session_state.current_session:
        session_info = st.session_state.chatbot.get_session_info(
            st.session_state.current_session.session_id
        )

        st.subheader("Session Info")
        st.write(f"**Session ID:** {session_info['session_id']}...")
        st.write(f"**Current Node:** {session_info['current_node']}")
        st.write(f"**Questions Asked:** {session_info['conversation_length']}")
        st.write(f"**Facts:** {session_info['client_information']}")

        # st.subheader("Progress")
        # fx_status = "Complete" if session_info["fx_completed"] else "⏳ In Progress"
        # ir_status = "Complete" if session_info["ir_completed"] else "⏳ Pending"
        # st.write(f"**FX Branch:** {fx_status}")
        # st.write(f"**IR Branch:** {ir_status}")

        if session_info["recommended_products"]:
            st.subheader("Products Identified")
            for product in session_info["recommended_products"]:
                st.write(f"• {product}")

        if st.button("End Session"):
            st.session_state.chatbot.end_session(
                st.session_state.current_session.session_id
            )
            st.session_state.current_session = None
            st.session_state.conversation_history = []
            st.rerun()

# Main content
if not st.session_state.current_session:
    st.markdown(
        """
    ## Welcome to the Global Markets Product Chatbot
    
    ### 🚀 Getting Started:
    Click **"Start New Chat"** in the sidebar to begin.
    """
    )

else:
    # Conversation history
    for message in st.session_state.conversation_history:
        with st.chat_message("user" if message["type"] == "user" else "assistant"):
            st.write(message["content"])

    # Client info phase
    if (
        st.session_state.current_session
        and st.session_state.current_session.current_node == "preprocessing"
    ):
        st.markdown("### Client Information Collection")
        st.markdown(
            "Provide any details about the client. We'll extract answers from this to skip questions later."
        )

        client_info = st.text_area(
            "Client Information:",
            placeholder="Example: The company is both an importer and exporter, mainly in EUR/USD.",
            height=150,
        ).strip()

        uploaded_file = st.file_uploader(
            "Upload client document (PDF, DOCX, or TXT):", type=["pdf", "docx", "txt"]
        )

        if st.button("Submit Client Info", use_container_width=True):
            try:
                # Process client input using modern extraction
                result = st.session_state.chatbot.process_client_input(
                    st.session_state.current_session.session_id, client_info
                )

                if result:
                    # Add to conversation history
                    if client_info:
                        st.session_state.conversation_history.append(
                            {
                                "type": "user",
                                "content": f"Client Info: {client_info}",
                            }
                        )
                        extracted_count = result.get("extracted_count", 0)
                        analysis_msg = (
                            f"Analyzed client information. Pre-answered {extracted_count} questions."
                            if extracted_count > 0
                            else "Client information recorded. Starting consultation..."
                        )
                    else:
                        analysis_msg = (
                            "Starting consultation without client information."
                        )

                    st.session_state.conversation_history.append(
                        {"type": "bot", "content": analysis_msg}
                    )

                    # Get the next question if available
                    if (
                        result["current_node"]
                        and result["current_node"] != "consultation_complete"
                    ):
                        current_node = st.session_state.chatbot.decision_tree.get_node(
                            result["current_node"]
                        )
                        if current_node:
                            response = (
                                st.session_state.chatbot._format_question_response(
                                    current_node
                                )
                            )
                            st.session_state.conversation_history.append(
                                {"type": "bot", "content": response}
                            )

                st.rerun()
            except Exception as e:
                st.error(f"Error processing client info: {e}")

    else:
        # Normal question nodes
        current_node = st.session_state.chatbot.decision_tree.get_node(
            st.session_state.current_session.current_node
        )
        if current_node:
            st.markdown(f"### {current_node.question}")
            for i, choice in enumerate(current_node.choices):
                if st.button(
                    f"{i+1}. {choice}", key=f"choice_{i}", use_container_width=True
                ):
                    try:
                        response = st.session_state.chatbot.process_client_choice(
                            st.session_state.current_session.session_id, choice
                        )
                        st.session_state.conversation_history.append(
                            {"type": "user", "content": f"Selected: {choice}"}
                        )
                        st.session_state.conversation_history.append(
                            {"type": "bot", "content": response}
                        )
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error processing response: {e}")
