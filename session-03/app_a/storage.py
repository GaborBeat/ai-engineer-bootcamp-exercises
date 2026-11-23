"""Reads the settings file and saves conversations to disk."""

import json
from datetime import datetime
from pathlib import Path

# These paths start from the folder this file is in, so the app finds its
# files no matter which folder you run it from.
APP_FOLDER = Path(__file__).parent
SETTINGS_FILE = APP_FOLDER / "settings.json"
CONVERSATIONS_FOLDER = APP_FOLDER / "conversations"


def load_settings():
    """Read settings.json and return it as a dictionary."""
    with open(SETTINGS_FILE) as file:
        return json.load(file)


def new_conversation_id():
    """Name a new conversation after the date and time, like 20261123_194207."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def save_conversation(settings, conversation_id, messages):
    """Write the conversation so far to its own JSON file."""
    CONVERSATIONS_FOLDER.mkdir(exist_ok=True)

    conversation = {
        "assistant": settings["assistant"]["name"],
        "model": settings["model"]["name"],
        "message_count": len(messages),
        "messages": messages,
    }
    with open(CONVERSATIONS_FOLDER / f"{conversation_id}.json", "w") as file:
        json.dump(conversation, file, indent=2)
