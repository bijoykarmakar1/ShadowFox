# AI Autocorrect Keyboard System

## ShadowFox AI/ML Internship - Task 1

This project is a Python-based AI application that performs:

- Spell Checking
- Next Word Prediction
- Session Statistics
- History Tracking

## Features

### Spell Checker
- Detects incorrect spellings.
- Suggests the top matching words.
- Uses PySpellChecker and NLTK.

### Next Word Prediction
- Predicts the next likely word.
- Uses Bigram and Trigram language models.
- Includes custom conversational data and NLP corpus.

### History Management
- Stores incorrect words and suggestions.
- Allows viewing and clearing history.

### Session Statistics
- Tracks:
  - Total words checked
  - Correct words
  - Incorrect words
  - Accuracy percentage

## Technologies Used

- Python 3
- NLTK
- PySpellChecker
- Difflib

## Project Structure

```
Autocorrect_Keyboard/
│
├── main.py
├── autocorrect.py
├── predictor.py
├── history.py
├── stats.py
├── utils.py
├── requirements.txt
├── history.txt
└── README.md
```

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

Run:

```
python main.py
```

## Author

Bijoy Karmakar

ShadowFox AI/ML Internship Project
