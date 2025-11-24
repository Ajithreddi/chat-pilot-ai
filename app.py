import streamlit as st
import requests
import uuid

from config import WEBHOOK_URL


st.set_page_config(page_title="AI Chat", page_icon="🤖")

# Init conversation
if "conversation" not in st.session_state:
    st.session_state["conversation"] = []

# Create a unique session ID for each user
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())


USER_PROMPT = st.chat_input("Enter your message")

if USER_PROMPT:
    # Add user msg
    st.session_state.conversation.append(
        {"role": "user", "data": USER_PROMPT}
    )

    # Call n8n
    response = requests.post(
        WEBHOOK_URL,
        json={ 
            "user_prompt": USER_PROMPT, 
            "sessionId": st.session_state.session_id
        }
    )
    
    if response.status_code == 200:
        ai_output = response.json()[0]["output"]
        st.session_state["conversation"].append(
            {"role": "ai", "data": ai_output}
        )
    else:
        st.session_state["conversation"].append(
            {"role": "ai", "data": f"Error {response.status_code}"}
        )

# Display messages
for con in st.session_state["conversation"]:
    with st.chat_message(con["role"]):
        st.write(con["data"])