from random import randint


TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_question_answer():
    rnd_num = randint(1, 100)
    correct_answer = "yes" if is_even(rnd_num) else "no"
    question = f"Question: {rnd_num}"
    return question, correct_answer
