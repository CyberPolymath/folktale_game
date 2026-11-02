# 🎯 KBC: Python Terminal Quiz

A fun, text-based quiz trivia game inspired by *Kaun Banega Crorepati*, built in pure Python. No external libraries and no setup, just run it in your terminal and test your own brain.

## 🧠 The Spirit of the Game

This game is meant to be played **honestly, on your own**.

- No AI assistants (ChatGPT, Claude, Gemini, etc.)
- No Googling
- No asking friends, family, or classmates

The only person you're competing against is yesterday's you. If you don't know an answer, guess, take the penalty, and learn from it. That's the whole point.

## 🎮 Features

- Multiple quiz categories (currently **Python Language** and **Basic Maths**)
- Multiple-choice questions with 4 options each
- Scoring: **+2** for every correct answer, **-1** for every wrong answer
- Live score after every question
- Final result with correct-answer count and maximum possible score
- Input validation, so typing something invalid never crashes the game
- **Infinitely extensible**: add as many questions and categories as you want

## 🚀 How to Run

**Requirements:** Python 3.6 or higher

```bash
python3 game.py
```

## 📜 How to Play

1. Start the game and choose a category by entering its number.
2. Read the rules shown on screen.
3. Answer each question by entering the option number (1-4).
4. See your final score when all questions are done.

## ➕ Extending the Game

### Add a question
Append a dictionary to any questions list:

```python
{
    "question": "Which symbol starts a comment in Python?",
    "options": ["//", "#", "/*", "--"],
    "answer": "#",
}
```

Nothing else needs to change. The game counts questions automatically.

### Add a new category

1. Create a new questions list (e.g. `gk_questions = [...]`).
2. Register it in the `categories` dictionary:

```python
"3": Category("General Knowledge", gk_questions),
```

### Change the scoring
Edit these constants at the top of the file:

```python
POINTS_CORRECT = 2
POINTS_WRONG = -1
```

## 🗺️ Ideas for the Future

- Shuffle questions and options on every run
- Lifelines (50-50, Skip, Flip the Question)
- Difficulty levels and prize-money ladder
- High-score saving to a file
- Timer for each question
- More categories: Operating Systems, General Knowledge, Science, and more

## 📄 License

Free to use, modify, and share for learning purposes.
