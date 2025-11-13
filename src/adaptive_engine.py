import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

class AdaptiveEngine:
    def __init__(self):
        self.model = DecisionTreeClassifier(max_depth=3)  # Lightweight
        self.difficulty_map = {'Easy': 0, 'Medium': 1, 'Hard': 2}
        self.le = LabelEncoder()
    
    def generate_synthetic_data(self, num_samples=1000):
        X = []
        y = []
        for _ in range(num_samples):
            current_diff = np.random.randint(0, 3)
            correctness = np.random.randint(0, 2)
            response_time = np.random.uniform(1, 30)  # Seconds, simulated
            
            # Simulate rules for next difficulty
            if correctness == 1 and response_time < 10:
                next_diff = min(current_diff + 1, 2)  # Increase if good
            elif correctness == 0 or response_time > 20:
                next_diff = max(current_diff - 1, 0)  # Decrease if struggling
            else:
                next_diff = current_diff  # Stay same
            
            X.append([current_diff, correctness, response_time])
            y.append(next_diff)
        
        return np.array(X), np.array(y)
    
    def train_model(self):
        X, y = self.generate_synthetic_data()
        self.model.fit(X, y)
    
    def predict_next_difficulty(self, current_diff_idx, correctness, response_time):
        input_data = np.array([[current_diff_idx, correctness, response_time]])
        prediction = self.model.predict(input_data)[0]
        return int(prediction)