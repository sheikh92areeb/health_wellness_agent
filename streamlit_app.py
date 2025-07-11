import streamlit as st
import config
from agents import Runner
from agent import build_health_welness_agent
from context import get_user_context
from utils.streaming import stream_agent_output

st.set_page_config(page_title="💪 Health & Wellness Agent", page_icon="💬")
st.title("💬 AI Health & Wellness Planner")
st.markdown("Start chatting with your wellness assistant:")

# Initialize context and chat history
if "context" not in st.session_state:
    st.session_state.context = get_user_context()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Show previous messages
for sender, msg in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(msg)

# Chat input
user_input = st.chat_input("Type your message...")

if user_input:
    # Append user message
    st.session_state.chat_history.append(("user", user_input))

    # Agent setup
    agent = build_health_welness_agent()

    # Assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = Runner.run_sync(
                starting_agent=agent,
                input=user_input,
                context=st.session_state.context
            )
            st.markdown(result.final_output)
            st.session_state.chat_history.append(("assistant", result.final_output))