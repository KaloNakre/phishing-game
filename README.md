# Cyber Phishing Detector Game

A **Python Flask web game** that helps users identify phishing URLs.  
The game is built with a **cyber-style UI**, using HTML, CSS, JS, and Python (Flask).  
Players enter their name, face 10 phishing/safe URL challenges, and get a **score and accuracy** at the end.  

---

## Features

- **Cyber-themed frontend** with matrix-style animation  
- **Randomly selects URLs** from a Kaggle phishing dataset  
- **Interactive game mechanics**: YES / NO buttons to identify phishing  
- **Accuracy calculation** and score summary  
- **Handles messy CSVs** with encoding and commas in URLs  

---

## Project Structure

```text
phishing-game/
│
├── app.py                     # Flask backend
├── game_engine.py             # Game logic (question generation, scoring, etc.)
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignore unnecessary files
│
├── dataset/                   # CSV dataset (not included in GitHub)
│   └── phishing_dataset.csv
│
├── templates/                 # HTML templates for Flask
│   ├── index.html             # Homepage (enter name)
│   ├── loading.html           # Loading screen
│   ├── game.html              # Main game page
│   └── result.html            # Game result and accuracy
│
└── static/                    # CSS and JavaScript files
    ├── css/
    │   └── style.css          # Styling for the web pages
    └── js/
        ├── game.js            # Game logic for buttons and UI
        └── matrix.js          # Cyber-style background animation