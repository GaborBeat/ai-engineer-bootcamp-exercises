[1mdiff --git a/session-03/app_a/streamlit_app.py b/session-03/app_a/streamlit_app.py[m
[1mindex bd55663..4605f34 100644[m
[1m--- a/session-03/app_a/streamlit_app.py[m
[1m+++ b/session-03/app_a/streamlit_app.py[m
[36m@@ -1,50 +1,107 @@[m
[31m-"""App A: the Session 1 assistant, grown to three files.[m
[32m+[m[32m"""Your personal AI assistant.[m
 [m
[31m-Run it from the top folder of the repository:[m
[31m-    streamlit run session-03/app_a/streamlit_app.py[m
[32m+[m[32mRun it from the terminal:[m
[32m+[m[32m    streamlit run app.py[m
 """[m
 [m
[32m+[m[32mimport os[m
[32m+[m[32mimport sqlite3[m
[32m+[m
 import openai[m
 import streamlit as st[m
[32m+[m[32mfrom dotenv import load_dotenv[m
[32m+[m
[32m+[m[32m# ---------- Part 1: the personality ----------[m
[32m+[m[32m# Change these to make the assistant your own.[m
[32m+[m[32mTITLE = "My AI Assistant"[m
[32m+[m[32mSYSTEM_PROMPT = """You are a friendly, helpful assistant.[m
[32m+[m[32mKeep your answers short: two or three sentences."""[m
[32m+[m
[32m+[m[32m# ---------- Settings ----------[m
[32m+[m[32mMODEL = "google/gemma-4-26b-a4b-it:floor"[m
[32m+[m[32mMAX_REPLY_TOKENS = 300  # the longest reply allowed, in tokens[m
[32m+[m[32mMAX_MESSAGES = 20  # the most messages one visitor can send in a chat[m
[32m+[m[32mCHAT_DB = os.path.join(os.path.dirname(__file__), "chat_history.db")[m
[32m+[m
[32m+[m[32m# On your Codespace, the key comes from .env. Once deployed, it comes[m
[32m+[m[32m# from the app's secrets. Either way, it never appears in this file.[m
[32m+[m[32mload_dotenv()[m
[32m+[m[32mclient = openai.OpenAI([m
[32m+[m[32m    base_url="https://openrouter.ai/api/v1",[m
[32m+[m[32m    api_key=os.environ["OPENROUTER_API_KEY"],[m
[32m+[m[32m)[m
[32m+[m
[32m+[m[32mdef load_messages():[m
[32m+[m[32m    """Load the saved conversation from the local SQLite database."""[m
[32m+[m[32m    with sqlite3.connect(CHAT_DB) as connection:[m
[32m+[m[32m        connection.execute([m
[32m+[m[32m            """[m
[32m+[m[32m            CREATE TABLE IF NOT EXISTS messages ([m
[32m+[m[32m                id INTEGER PRIMARY KEY AUTOINCREMENT,[m
[32m+[m[32m                role TEXT NOT NULL,[m
[32m+[m[32m                content TEXT NOT NULL[m
[32m+[m[32m            )[m
[32m+[m[32m            """[m
[32m+[m[32m        )[m
[32m+[m[32m        rows = connection.execute([m
[32m+[m[32m            "SELECT role, content FROM messages ORDER BY id"[m
[32m+[m[32m        ).fetchall()[m
[32m+[m[32m    return [{"role": role, "content": content} for role, content in rows][m
[32m+[m
 [m
[31m-from assistant import get_reply[m
[31m-from storage import load_settings, new_conversation_id, save_conversation[m
[32m+[m[32mdef save_message(role, content):[m
[32m+[m[32m    """Append one message to the persistent conversation."""[m
[32m+[m[32m    with sqlite3.connect(CHAT_DB) as connection:[m
[32m+[m[32m        connection.execute([m
[32m+[m[32m            "INSERT INTO messages (role, content) VALUES (?, ?)",[m
[32m+[m[32m            (role, content),[m
[32m+[m[32m        )[m
 [m
[31m-settings = load_settings()[m
[31m-st.title(settings["assistant"]["name"])[m
 [m
[31m-# ---------- Part 1: this chat's history ----------[m
[31m-# Streamlit runs this whole file again after every message. session_state[m
[31m-# is the one place that survives, so the conversation lives there.[m
[31m-if "messages" not in st.session_state:[m
[31m-    st.session_state.messages = [][m
[31m-    st.session_state.conversation_id = new_conversation_id()[m
[32m+[m[32mdef clear_messages():[m
[32m+[m[32m    """Delete the saved conversation."""[m
[32m+[m[32m    with sqlite3.connect(CHAT_DB) as connection:[m
[32m+[m[32m        connection.execute("DELETE FROM messages")[m
 [m
[31m-for message in st.session_state.messages:[m
[32m+[m
[32m+[m[32mst.title(TITLE)[m
[32m+[m
[32m+[m[32m# ---------- Part 2: persistent chat history ----------[m
[32m+[m[32m# Conversation messages are stored in SQLite, so they survive browser[m
[32m+[m[32m# refreshes and Streamlit reruns (and app restarts if the disk persists).[m
[32m+[m[32mif st.button("Clear chat"):[m
[32m+[m[32m    clear_messages()[m
[32m+[m[32m    st.rerun()[m
[32m+[m
[32m+[m[32mmessages = load_messages()[m
[32m+[m
[32m+[m[32mfor message in messages:[m
     st.chat_message(message["role"]).write(message["content"])[m
 [m
[31m-# ---------- Part 2: the cap ----------[m
[31m-# Every message costs money, so one visitor can only send so many.[m
[31m-max_messages = settings["limits"]["max_messages"][m
[31m-messages_sent = len([m for m in st.session_state.messages if m["role"] == "user"])[m
[31m-if messages_sent >= max_messages:[m
[32m+[m[32mmessages_sent = sum(1 for message in messages if message["role"] == "user")[m
[32m+[m[32mif messages_sent >= MAX_MESSAGES:[m
     st.info("You've reached the message limit for this chat. Thanks for trying it out!")[m
     st.stop()[m
 [m
[31m-# ---------- Part 3: one message, from the text box to the reply ----------[m
[32m+[m[32m# ---------- Part 3: the call ----------[m
 user_text = st.chat_input("Say something")[m
 if user_text:[m
[31m-    st.session_state.messages.append({"role": "user", "content": user_text})[m
[32m+[m[32m    save_message("user", user_text)[m
[32m+[m[32m    messages.append({"role": "user", "content": user_text})[m
     st.chat_message("user").write(user_text)[m
 [m
     try:[m
[31m-        reply = get_reply(settings, st.session_state.messages)[m
[32m+[m[32m        response = client.chat.completions.create([m
[32m+[m[32m            model=MODEL,[m
[32m+[m[32m            # The personality goes first, then the conversation so far[m
[32m+[m[32m            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,[m
[32m+[m[32m            max_tokens=MAX_REPLY_TOKENS,[m
[32m+[m[32m        )[m
     except openai.APIError as error:[m
[31m-        st.session_state.messages.pop()  # forget the message that didn't get a reply[m
[32m+[m[32m        # Keep the user message in history so they can retry or refer to it.[m
         st.error(f"Couldn't get a reply from the model: {error}")[m
         st.stop()[m
 [m
[31m-    st.session_state.messages.append({"role": "assistant", "content": reply})[m
[31m-    st.chat_message("assistant").write(reply)[m
[31m-[m
[31m-    save_conversation(settings, st.session_state.conversation_id, st.session_state.messages)[m
[32m+[m[32m    reply = response.choices[0].message.content or "(The model sent back an empty reply.)"[m
[32m+[m[32m    save_message("assistant", reply)[m
[32m+[m[32m    st.chat_message("assistant").write(reply)[m
\ No newline at end of file[m
