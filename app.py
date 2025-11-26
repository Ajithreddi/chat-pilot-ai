import os
import sys
import uuid
import requests
import streamlit as st

# Add project root to path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

# Import environment settings
from config.settings import ENV, WEBHOOK_URL

# Page setup
st.set_page_config(page_title="ChatPilot AI 99", page_icon="🤖")

# Sidebar
with st.sidebar:
    st.title("🤖 AI Mode")

    # Show environment
    st.markdown(f"### 🏷️ Environment: **{ENV}**")

    ai_mode = st.selectbox(
        "Choose a mode",
        ["ChatPilot Tutor 📚", "Creative Lab ✨", "Play Zone 🎮", "Chill Buddy 😄"]
    )

    st.markdown("### ⚡ Quick Actions")
    summarize_clicked = st.button("📝 Summarize Conversation")
    simplify_clicked = st.button("✨ Explain Simply")

# Header
st.markdown("""
<h1 style='text-align:center;'>ChatPilot AI 🤖</h1>
<p style='text-align:center; color:grey;'>Your personal learning assistant.</p>
""", unsafe_allow_html=True)

# Session storage
if "conversation" not in st.session_state:
    st.session_state.conversation = []

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Input
user_prompt = st.chat_input("Ask something...")

if summarize_clicked:
    user_prompt = "Summarize the above conversation clearly."

if simplify_clicked:
    user_prompt = "Explain the previous message in simple terms."

# Handle input
if user_prompt:
    st.session_state.conversation.append({"role": "user", "data": user_prompt})

    payload = {
        "user_prompt": user_prompt,
        "ai_mode": ai_mode,
        "sessionId": st.session_state.session_id
    }

    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        if response.status_code == 200:
            ai_reply = response.json()[0].get("output", "No response received.")
        else:
            ai_reply = f"Error {response.status_code}"
    except Exception as e:
        ai_reply = f"Request failed: {e}"

    st.session_state.conversation.append({"role": "ai", "data": ai_reply})

# Chat UI
for msg in st.session_state.conversation:
    with st.chat_message(msg["role"]):
        st.write(msg["data"])
