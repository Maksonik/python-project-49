import random
import operator

from brain_games.scripts.engine import play_game

DESCRIPTION = 'What is the result of the expression?'


def generate_question():
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operation = random.choice(list(operations.keys()))
    question = f'{num1} {operation} {num2}'
    correct_answer = str(operations[operation](num1, num2))
    return question, correct_answer


def main():
    play_game(generate_question, DESCRIPTION)


if __name__ == '__main__':
    main()
