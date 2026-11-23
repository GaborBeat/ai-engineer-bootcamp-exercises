# Sage: a terminal study coach

Sage is a small chat assistant that runs in the terminal. It coaches you while you learn to code: short answers, and a question back to check you understood.

## Features

- A persona you can change without touching the code (see `settings.json`)
- Conversation memory, limited to the most recent turns (`history.max_turns`)
- Every conversation saved to the `sessions` folder as JSON
- Graceful error handling, so the chat never crashes
- Optional stats after each reply: messages sent and tokens used

## Run it

Your API key should already be saved in the `.env` file at the top of the repository.

```
python main.py
```

Type a message and press Enter. Type `quit` to leave.

## Settings

| Setting | What it does |
| --- | --- |
| `assistant.name` | The name shown before each reply |
| `assistant.persona` | Role, tone, and rules that shape the system prompt |
| `model.name` | Which model to call |
| `model.max_tokens` | The longest reply allowed, in tokens |
| `model.temperature` | How varied the replies are |
| `history.max_turns` | How many recent turns the assistant remembers |
| `storage.folder` | Where conversations are saved |
| `display.show_stats` | Show the stats line after each reply |
| `commands.quit` | Words that end the chat |

## Files

- `main.py`: the chat loop
- `model.py`: builds the prompt and calls the model
- `storage.py`: loads settings and saves conversations
- `settings.json`: everything you can change
