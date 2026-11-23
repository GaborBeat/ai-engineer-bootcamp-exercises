"""App A: the Session 1 assistant, grown to three files.

Run it from the top folder of the repository:
    streamlit run session-03/app_a/streamlit_app.py
"""

import openai
import streamlit as st

from assistant import get_reply
from storage import load_settings, new_conversation_id, save_conversation

settings = load_settings()
st.title(settings["assistant"]["name"])

# ---------- Part 1: this chat's history ----------
# Streamlit runs this whole file again after every message. session_state
# is the one place that survives, so the conversation lives there.
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.conversation_id = new_conversation_id()

for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# ---------- Part 2: the cap ----------
# Every message costs money, so one visitor can only send so many.
max_messages = settings["limits"]["max_messages"]
messages_sent = len([m for m in st.session_state.messages if m["role"] == "user"])
if messages_sent >= max_messages:
    st.info("You've reached the message limit for this chat. Thanks for trying it out!")
    st.stop()

# ---------- Part 3: one message, from the text box to the reply ----------
user_text = st.chat_input("Say something")
if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})
    st.chat_message("user").write(user_text)

    try:
        reply = get_reply(settings, st.session_state.messages)
    except openai.APIError as error:
        st.session_state.messages.pop()  # forget the message that didn't get a reply
        st.error(f"Couldn't get a reply from the model: {error}")
        st.stop()

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)

    save_conversation(settings, st.session_state.conversation_id, st.session_state.messages)
