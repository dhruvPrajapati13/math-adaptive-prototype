class PerformanceTracker:
    def __init__(self):
        self.performances = []
    
    def add_performance(self, difficulty, correctness, response_time):
        self.performances.append({
            'difficulty': difficulty,
            'correctness': correctness,
            'response_time': response_time
        })
    
    def get_summary(self):
        if not self.performances:
            return {'accuracy': 0, 'avg_time': 0}
        
        total_correct = sum(p['correctness'] for p in self.performances)
        accuracy = total_correct / len(self.performances)
        avg_time = sum(p['response_time'] for p in self.performances) / len(self.performances)
        
        return {'accuracy': accuracy, 'avg_time': avg_time}