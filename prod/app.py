import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import streamlit as st
import requests
import uuid
from config.settings import ENV, WEBHOOK_URL


st.set_page_config(page_title="ChatPilot AI Killer", page_icon="🤖")

# Header
st.markdown("""
<h1 style='text-align:center; font-size:40px;'>ChatPilot AI 🤖</h1>
<p style='text-align:center; font-size:18px; color:grey;'>
A simple, fast, and smart learning assistant.
</p>
<hr>
""", unsafe_allow_html=True)

# Session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())


# AI modes (Sidebar)

st.sidebar.header("🤖 AI Mode")

ai_mode = st.sidebar.selectbox(
    "Choose a ChatPilot Mode",
    [
        "ChatPilot Tutor 📚",
        "Creative Lab ✨",
        "Play Zone 🎮",
        "Chill Buddy 😄"
    ]
)


# Quick Actions (Sidebar)
st.sidebar.markdown("### ⚡ Quick Actions")
summarize_clicked = st.sidebar.button("📝 Summarize")
simple_clicked = st.sidebar.button("✨ Explain Simply")

# Chat Input
USER_PROMPT = st.chat_input("Enter your message")

if summarize_clicked:
    USER_PROMPT = "Summarize the above conversation clearly."
elif simple_clicked:
    USER_PROMPT = "Explain the previous message in very simple terms."


# Process message
if USER_PROMPT:
    st.session_state.conversation.append({"role": "user", "data": USER_PROMPT})

    response = requests.post(
        WEBHOOK_URL,
        json={
            "user_prompt": USER_PROMPT,
            "ai_mode": ai_mode,
            "sessionId": st.session_state.session_id
        }
    )

    if response.status_code == 200:
        ai_reply = response.json()[0]["output"]
    else:
        ai_reply = f"Error {response.status_code}"

    st.session_state.conversation.append({"role": "ai", "data": ai_reply})


# Display chat
for con in st.session_state.conversation:
    with st.chat_message(con["role"]):
        st.write(con["data"])

