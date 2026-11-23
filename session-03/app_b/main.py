"""Sage: a study coach you chat with in the terminal.

Run it from the terminal:
    python main.py
"""

from datetime import datetime

from model import ask_model, create_client
from storage import load_settings, save_session


def main():
    settings = load_settings()
    client = create_client()

    name = settings["assistant"]["name"]
    quit_words = settings["commands"]["quit"]
    session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    history = []
    turn = 0

    print(f"{name} is ready. Type a message, or '{quit_words[0]}' to leave.")

    while True:
        user_text = input("\nYou: ").strip()

        if user_text.lower() in quit_words:
            break
        if not user_text:
            print("(Type a message first.)")
            continue

        turn += 1
        history.append({"role": "user", "content": user_text})

        result = ask_model(client, settings, history)
        if result is None:
            continue

        history.append({"role": "assistant", "content": result["reply"]})
        print(f"\n{name}: {result['reply']}")

        if settings["display"].get("show_stats", False):
            print(
                f"[turn {turn}: sent {result['messages_sent']} messages, "
                f"{result['tokens_in']} tokens in, {result['tokens_out']} tokens out]"
            )

        save_session(settings, session_id, history)

    print(f"\nGoodbye! We talked for {turn} turns.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
