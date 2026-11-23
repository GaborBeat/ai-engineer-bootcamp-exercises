# App A: Pip, a trivia host

This is the Session 1 assistant, grown from one file to three. It does the same job: you type a message in the browser, and the model replies in a personality set by a system prompt. Two things are new: the settings live in their own file, and every conversation is saved to disk.

## Run it

From the top folder of the repository:

```
streamlit run session-03/app_a/streamlit_app.py
```

Your API key should already be saved in the `.env` file at the top of the repository. The packages this app needs are listed in `requirements.txt`, also at the top of the repository.

## Files

- `streamlit_app.py`: the entry point. The page, the chat history, the message cap, and the path one message takes
- `assistant.py`: connects to the model and gets one reply
- `storage.py`: reads the settings and saves conversations
- `settings.json`: the assistant's name and system prompt, the model, and the message cap
- `conversations/`: appears after the first reply. One JSON file per conversation

## Settings

| Setting | What it does |
| --- | --- |
| `assistant.name` | The title at the top of the page |
| `assistant.system_prompt` | The personality: sent to the model first, on every call |
| `model.name` | Which model to call |
| `model.max_reply_tokens` | The longest reply allowed, in tokens |
| `limits.max_messages` | The most messages one visitor can send in a chat |
