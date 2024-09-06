from brain_games.scripts.cli import welcome_user
import prompt


def play_game(game, description):
    name = welcome_user()
    print(description)

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        question, correct_answer = game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')