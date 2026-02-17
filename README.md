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

phishing-game/
│
├── app.py # Flask backend
├── game_engine.py # Game logic
├── requirements.txt # Python dependencies
├── .gitignore # Ignore unnecessary files
│
├── dataset/ # CSV dataset 
│ └── phishing_dataset.csv
│
├── templates/ # HTML templates
│ ├── index.html
│ ├── loading.html
│ ├── game.html
│ └── result.html
│
└── static/ # CSS and JS
├── css/
│ └── style.css
└── js/
├── game.js
└── matrix.js