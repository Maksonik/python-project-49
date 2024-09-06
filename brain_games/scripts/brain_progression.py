import random

from brain_games.scripts.engine import play_game


DESCRIPTION = 'What number is missing in the progression?'


def generate_progression():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = [start + i * step for i in range(length)]
    return progression


def generate_question():
    progression = generate_progression()
    missing_index = random.randint(0, len(progression) - 1)
    correct_answer = str(progression[missing_index])
    progression[missing_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer


def main():
    play_game(generate_question, DESCRIPTION)


if __name__ == '__main__':
    main()
