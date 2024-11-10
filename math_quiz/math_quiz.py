import random

def generate_random_integer(min_value, max_value):
    """
    Generates a random integer between min_value and max_value and return.

    """
    return random.randint(min_value, max_value)

def generate_random_operator():
    """
    Selects a random operator from a list of operators +,-,* and return one.
    """
    return random.choice(['+', '-', '*'])

def math_problem(num1, num2, operator):
    """
    Creates a math problem string and calculates the correct answer and returnntuple containing the math problem as a string and the correct answer.
    """
    problem = f"{num1} {operator} {num2}"
    
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return problem, answer

def math_quiz():
    """
    Main function to run the Math Quiz game.
    """
    score = 0
    total_questions = 3 

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 10)  
        operator = generate_random_operator()

        problem, correct_answer = math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
