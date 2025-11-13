import random

def generate_puzzle(difficulty):
    operations = ['+', '-', '*', '/']
    op = random.choice(operations)
    
    if difficulty == 'Easy':
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        if op == '/':
            num1 = num2 * random.randint(1, 5)  # Ensure integer division
    elif difficulty == 'Medium':
        num1 = random.randint(10, 50)
        num2 = random.randint(5, 20)
        if op == '/':
            num1 = num2 * random.randint(1, 10)
    elif difficulty == 'Hard':
        num1 = random.randint(50, 100)
        num2 = random.randint(10, 50)
        if op == '/':
            num1 = num2 * random.randint(1, 20)
    else:
        raise ValueError("Invalid difficulty")
    
    problem = f"{num1} {op} {num2}"
    
    if op == '+':
        answer = num1 + num2
    elif op == '-':
        answer = num1 - num2
    elif op == '*':
        answer = num1 * num2
    elif op == '/':
        answer = num1 // num2  # Integer division for simplicity
    
    return problem, answer