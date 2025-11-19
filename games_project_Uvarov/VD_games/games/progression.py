import random

DESCRIPTION = 'What number is missing in the progression?'

def generate_round():
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    length = random.randint(5, 10)

    progression = list(range(start, start + length * step, step))

    hidden_index = random.randint(0, length - 1)

    correct_answer = str(progression[hidden_index])

    progression[hidden_index] = '..'

    question = ' '.join(map(str, progression))

    return question, correct_answer
