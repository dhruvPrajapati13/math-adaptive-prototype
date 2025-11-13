# Maths AI-Powered Adaptive Learning Prototype

## Objective
Build a minimal adaptive math learning prototype that adjusts puzzle difficulty based on user performance using a lightweight ML model (DecisionTreeClassifier from scikit-learn). The goal is to demonstrate how AI can personalize learning difficulty dynamically for children aged 5-10 practicing basic math (addition, subtraction, multiplication, division).

## Features
- Generate simple math puzzles at 3 difficulty levels (Easy, Medium, Hard).
- Track performance (correctness, response time).
- Use ML to adjust difficulty based on performance.
- Display end-of-session summary (accuracy, average time, recommended next level).

## Setup
1. Create your virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

## How It Works
- User enters name and chooses initial difficulty.
- System generates puzzles, tracks responses, and adapts difficulty using a pre-trained ML model on synthetic data.
- Session ends after 10 questions with a summary.

## Files
- `main.py`: Entry point for the console app.
- `puzzle_generator.py`: Generates math puzzles.
- `tracker.py`: Tracks user performance.
- `adaptive_engine.py`: Handles the ML-based adaptive logic.

## Extending
- For a web interface, install Streamlit and create an `app.py` that wraps the logic.
- Improve the ML by collecting real user data over time.
