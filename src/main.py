import time
from puzzle_generator import generate_puzzle
from tracker import PerformanceTracker
from adaptive_engine import AdaptiveEngine

def main():
    print("Welcome to Maths AI-Powered Adaptive Learning Prototype!")
    name = input("Enter your name: ")
    difficulties = ['Easy', 'Medium', 'Hard']
    print("Choose initial difficulty: 1. Easy, 2. Medium, 3. Hard")
    initial_idx = int(input("Enter number: ")) - 1
    current_difficulty = difficulties[initial_idx]

    tracker = PerformanceTracker()
    engine = AdaptiveEngine()
    engine.train_model()  # Train on synthetic data

    num_questions = 10  # Configurable session length
    for i in range(num_questions):
        problem, answer = generate_puzzle(current_difficulty)
        print(f"\nQuestion {i+1}: {problem}")
        
        start_time = time.time()
        user_answer = input("Your answer: ")
        end_time = time.time()
        
        try:
            user_answer = float(user_answer)
        except ValueError:
            user_answer = None  # Invalid input treated as wrong
        
        correctness = 1 if user_answer == answer else 0
        response_time = end_time - start_time
        
        tracker.add_performance(current_difficulty, correctness, response_time)
        
        # Adapt difficulty using ML
        current_idx = difficulties.index(current_difficulty)
        next_difficulty_idx = engine.predict_next_difficulty(current_idx, correctness, response_time)
        current_difficulty = difficulties[next_difficulty_idx]
        
        print(f"Correct: {'Yes' if correctness else 'No'} | Time: {response_time:.2f}s | Next difficulty: {current_difficulty}")

    # Summary
    summary = tracker.get_summary()
    print("\nSession Summary:")
    print(f"Accuracy: {summary['accuracy']:.2%}")
    print(f"Average Response Time: {summary['avg_time']:.2f}s")
    print(f"Final Difficulty: {current_difficulty}")
    print("Performance Log:")
    for log in tracker.performances:
        print(log)

if __name__ == "__main__":
    main()