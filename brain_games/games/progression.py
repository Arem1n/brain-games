from random import randint


TASK = 'What number is missing in the progression?'


def is_even(num):
    return num % 2 == 0


def get_question_answer():
    step_progression = randint(1, 10)
    first_element = randint(1, 100)
    len_progression = randint(5, 10)
    hidden_element = randint(1, len_progression)
    progression = ''

    for i in range(1, len_progression + 1):
        if i == hidden_element:
            correct_answer = str(first_element + step_progression * (i - 1))
            progression += '.. '
            continue
        progression += str(first_element + step_progression * (i - 1)) + ' '

    progression = progression.strip()

    question = f"Question: {progression}"
    return question, correct_answer
