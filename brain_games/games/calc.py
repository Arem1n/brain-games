from random import randint, choice


TASK = 'What is the result of the expression?'

operators = ['*', '-', '+']


def get_question_answer():
    first_operand = randint(0, 100)
    second_operand = randint(0, 100)
    operator = choice(operators)
    question = f"Question: {first_operand} {operator} {second_operand}"

    if operator == '+':
        correct_answer = first_operand + second_operand
    elif operator == '-':
        correct_answer = first_operand - second_operand
    else:
        correct_answer = first_operand * second_operand

    correct_answer = str(correct_answer)

    return question, correct_answer
