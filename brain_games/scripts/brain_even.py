import random

from brain_games.scripts.engine import play_game


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def play_round():
    number = random.randint(1, 100)
    question = f'Question: {number}'
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer


def main():
    play_game(play_round, DESCRIPTION)


if __name__ == '__main__':
    main()
