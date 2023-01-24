from random import randint
from math import gcd


TASK = 'Find the greatest common divisor of given numbers.'


def get_question_answer():
    num1 = randint(1, 100)
    num2 = randint(1, 100)
    correct_answer = str(gcd(num1, num2))
    question = f"Question: {num1} {num2}"
    return question, correct_answer
