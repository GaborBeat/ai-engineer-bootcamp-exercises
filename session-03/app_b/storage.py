"""Reading the settings file and saving conversations."""

import json
from datetime import datetime
from pathlib import Path

APP_FOLDER = Path(__file__).parent
SETTINGS_FILE = APP_FOLDER / "settings.json"


def load_settings():
    """Read settings.json into a dictionary."""
    with open(SETTINGS_FILE) as file:
        return json.load(file)


def save_session(settings, session_id, history):
    """Write the whole conversation to a JSON file in the sessions folder."""
    folder = APP_FOLDER / settings["storage"]["folder"]
    folder.mkdir(exist_ok=True)

    session = {
        "assistant": settings["assistant"]["name"],
        "saved_at": datetime.now().isoformat(timespec="seconds"),
        "turns": len(history) // 2,
        "messages": history,
    }
    with open(folder / f"session_{session_id}.json", "w") as file:
        json.dump(session, file, indent=2)
