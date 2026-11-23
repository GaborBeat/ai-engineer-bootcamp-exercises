"""Path drills: find a value inside nested data.

For each drill:
  1. Read the drill.
  2. Write what you expect on the "My prediction" line.
  3. Run this file and compare:
         python session-03/path_drills.py

Two files in the drill_data folder hold the data:
  saved_conversation.json   a chat saved by App A
  api_response.json         what the model's API sends back for one call
"""

import json
from pathlib import Path

DATA_FOLDER = Path(__file__).parent / "drill_data"

with open(DATA_FOLDER / "saved_conversation.json") as file:
    conversation = json.load(file)

with open(DATA_FOLDER / "api_response.json") as file:
    response = json.load(file)

# ---------- Step 0: look before you index ----------
# Remove the # from one of these lines, run the file, and read the structure.
# Put the # back when you are done.
# print(json.dumps(conversation, indent=2))
# print(json.dumps(response, indent=2))

# ---------- Drills 1 and 2: read the path, predict the value ----------

# Drill 1
# My prediction:
print("Drill 1:", conversation["assistant"])

# Drill 2
# My prediction:
print("Drill 2:", conversation["messages"][0]["content"])

# ---------- Drills 3 and 4: write the path yourself ----------

# Drill 3: the text of the LAST message in the saved conversation.
# Replace None with a path that starts with conversation[
drill_3 = None
print("Drill 3:", drill_3)

# Drill 4: the reply text inside the API response.
# Replace None with a path that starts with response[
drill_4 = None
print("Drill 4:", drill_4)

# ---------- Drills 5 and 6: a value, or an error? ----------
# Each of these might end in an error. Predict which, and name the error.
# Remove the # from the print line of drill 5 and run. Then put the # back
# before you try drill 6.

# Drill 5
# My prediction:
# print("Drill 5:", response["usage"]["total"])

# Drill 6
# My prediction:
# print("Drill 6:", conversation["messages"][6]["content"])
