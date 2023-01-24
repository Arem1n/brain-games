from random import randint


TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def get_question_answer():
    rnd_num = randint(2, 100)
    correct_answer = "yes" if is_prime(rnd_num) else "no"
    question = f"Question: {rnd_num}"
    return question, correct_answer
