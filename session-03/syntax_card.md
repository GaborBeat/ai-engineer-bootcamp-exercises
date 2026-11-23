# Syntax card: the Python in Apps A and B

You already know variables, `if`, loops, functions, lists, dictionaries and strings. These are the other pieces of Python you will meet tonight. You do not need to memorize them. When a line stops you, find its shape here.

| When you see | It means | Where |
| --- | --- | --- |
| `"""Some text."""` at the top of a file or function | A note for the reader. Python does nothing with it | every file |
| `import json` | Use a tool that comes with Python | `storage.py` |
| `from storage import load_settings` | Use one function from another file in this folder (`storage.py`) | A: `streamlit_app.py`, B: `main.py` |
| `f"{name} is ready"` | A string with a value dropped in where the `{ }` are | both apps |
| `settings["model"]["name"]` | Two lookups, left to right: get `"model"`, then get `"name"` inside it | both apps |
| `data.get("temperature", 0.7)` | Look up a key. If it is missing, use `0.7` instead of stopping with an error | B: `model.py`, `main.py` |
| `"messages" not in st.session_state` | True when that name is not there yet | A: `streamlit_app.py` |
| `[m for m in messages if m["role"] == "user"]` | A new list holding only the items that pass the test | A: `streamlit_app.py` |
| `[system_message] + history` | Two lists joined into one new list | A: `assistant.py`, B: `model.py` |
| `history.append(item)` and `messages.pop()` | Add one item to the end of a list; remove the last item | both apps |
| `turn += 1` and `prompt += "text"` | Add to what is already there: `turn = turn + 1` | B: `main.py`, `model.py` |
| `len(history) // 2` | Divide and drop the remainder: `7 // 2` is `3` | B: `storage.py` |
| `reply or "(empty)"` | Use `reply`, unless it is empty; then use the fallback | A: `assistant.py` |
| `while True:` with `break` and `continue` | Repeat forever. `break` leaves the loop; `continue` skips to the next time around | B: `main.py` |
| `input("You: ")` | Wait for the person to type a line, and give it back as a string | B: `main.py` |
| `text.strip()` and `text.lower()` | A copy with the spaces trimmed off the ends; a copy in lower case | B: `main.py` |
| `try:` ... `except SomeError as error:` | Try these lines. If that kind of error happens, run the `except` lines instead of stopping | A: `streamlit_app.py`, B: `model.py` |
| `return None` and `if result is None:` | `None` means "nothing here". `is None` checks for it | B: `model.py`, `main.py` |
| `with open(path) as file:` | Open a file, use it in the indented lines, and close it afterwards | `storage.py` |
| `json.load(file)` and `json.dump(data, file, indent=2)` | Read JSON text from a file into dictionaries and lists; write them back out as neatly indented JSON | `storage.py` |
| `Path(__file__).parent / "settings.json"` | The path to `settings.json` in the same folder as this code file | `storage.py` |
| `folder.mkdir(exist_ok=True)` | Create the folder. If it already exists, carry on | `storage.py` |
| `datetime.now().strftime("%Y%m%d_%H%M%S")` | The date and time right now, as text like `20261123_194207` | A: `storage.py`, B: `main.py` |
| `os.environ["OPENROUTER_API_KEY"]` | Read a secret value by name, so it never appears in the code | A: `assistant.py`, B: `model.py` |
| `st.title(...)`, `st.chat_input(...)`, `st.session_state` | Streamlit commands: draw something on the page, read what was typed, or remember a value between reruns | A: `streamlit_app.py` |
| `client.chat.completions.create(...)` | The call to the model: send the messages, get a response back | A: `assistant.py`, B: `model.py` |
| `if __name__ == "__main__":` | Run the lines below only when this file is the one you started | B: `main.py` |

Still stuck on a line? Mark it `# ?` and move on. A line you cannot read yet is a question to test, not a reason to stop.
