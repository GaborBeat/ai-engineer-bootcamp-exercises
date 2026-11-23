"""Talks to the language model."""

import os

from dotenv import load_dotenv
from openai import OpenAI

# Read the key from the .env file, then connect to OpenRouter with it.
# The key never appears in this file.
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
)


def get_reply(settings, messages):
    """Send the whole conversation to the model and return the reply text."""
    # The personality goes first, then the conversation so far.
    system_message = {"role": "system", "content": settings["assistant"]["system_prompt"]}

    response = client.chat.completions.create(
        model=settings["model"]["name"],
        messages=[system_message] + messages,
        max_tokens=settings["model"]["max_reply_tokens"],
    )
    return response.choices[0].message.content or "(The model sent back an empty reply.)"
