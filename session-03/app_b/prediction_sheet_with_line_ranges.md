# App B prediction sheet: Sage

Name:

**Predict before you run, so the run can prove you wrong.** A wrong prediction is a good result on this sheet, as long as you find the line you misread.

## How this works

1. **Read and predict (12 minutes).** Open the files in `session-03/app_b`: start with `README.md`, then `settings.json`, `main.py`, `model.py` and `storage.py`. Write an answer on every "My prediction" line. Do not run the app yet, and do not ask an assistant.
2. **Compare (6 minutes).** Your instructor names two questions. Share your predictions for those.
3. **Run and score (12 minutes).** For each question, follow "How to check". Fill in "What happened" and "The line that explains it".

To run the app, type these two lines in the terminal:

```
cd session-03/app_b
python main.py
```

## Scoring

| For each question | Points |
| --- | --- |
| You wrote a prediction before running, and you checked it | 1 |
| You named the file and line that explains what happened | +2 |
| Your prediction was right | +1 |

A wrong prediction with the line named (3 points) beats a lucky guess (2 points). Aim for at least four of the six questions predicted and checked.

## 1. The empty message

You start the app and press Enter without typing anything. What appears on the screen? Is anything sent to the model?

Where to look: `main.py`, lines 27 to 33

- My prediction:
- How to check: Run `python main.py`. Press Enter with nothing typed. Then type `quit`.
- What happened:
- The line that explains it (file and line number):

## 2. The eighth turn

You send eight messages in one chat. On the eighth, how many messages in total does the app send to the model? Write a number.

Where to look: `model.py`, lines 31 to 34, and `main.py`, lines 36 and 42

- My prediction:
- How to check: Run the app and send eight short messages (one word each is fine). After the eighth reply, read the line in square brackets: `[turn 8: sent ... messages, ...]`.
- What happened:
- The line that explains it (file and line number):

## 3. What is saved, and when

What file does the app create? What is inside it? At what moment is it written? Is anything written when you quit?

Where to look: `storage.py`, lines 17 to 29, and `main.py`, line 51

- My prediction:
- How to check: Run the app and type `quit` straight away. Look in the `app_b` folder: is there anything new? Run it again, send one message, and look again. Open the new file. Type `quit` and see whether the file changed.
- What happened:
- The line that explains it (file and line number):

## 4. Where the personality comes from

Sage sounds encouraging. Which file and line would you change to make Sage sarcastic? Which lines of code turn that setting into the instructions the model receives?

Where to look: `settings.json`, lines 4 to 11, and `model.py`, lines 18 to 28

- My prediction:
- How to check: Make your change, save the file, run the app, and send a message. Then put the file back the way it was (Ctrl+Z, or Cmd+Z on a Mac) and save.
- What happened:
- The line that explains it (file and line number):

## 5. A missing setting

In `settings.json`, line 16, change `"temperature"` to `"temperatur"`. The setting the code looks for is now missing. You run the app and send a message. What happens?

Where to look: `model.py`, line 45

- My prediction:
- How to check: Make the change, save, run the app, and send a message. Then undo the change and save.
- What happened:
- The line that explains it (file and line number):

## 6. Another missing setting

In `settings.json`, line 6, change `"tone"` to `"tonee"`. You run the app and send a message. What happens? Is it the same as question 5?

Where to look: `model.py`, line 24 and lines 37 to 55, and `main.py`, lines 38 to 40

- My prediction:
- How to check: Make the change, save, run the app, and send two messages. Type `quit`. Then undo the change and save.
- What happened:
- The line that explains it (file and line number):

## My score

Total: ___ out of 24

## Part 2: Verdict (after the debrief)

Would you trust this app, fix it, or throw it out? Give two reasons, each with a file and a line number.

- My verdict:
- Reason 1 (file and line):
- Reason 2 (file and line):

## Part 3: The fix (studio)

You direct an assistant to fix one problem in `model.py`, then check its work.

- What I asked (paste your message to the assistant):
- What changed (which lines, in your own words):
- What I predicted would happen when I ran it:
- What happened:

## Hand it in

1. Click the Source Control icon on the left side of the editor.
2. Type a short message, such as "Session 3 prediction sheet".
3. Click **Commit**, then **Sync Changes**.
4. Post the link to your fork in Discord.
