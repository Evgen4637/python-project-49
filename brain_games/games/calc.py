from brain_games.cli import welcome_user
from brain_games.moduls.rand import rand_num, rand_sign
from brain_games.moduls.utils import check_answer


def calc():
    name = welcome_user()
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    num = 0

    while num < 3:
        x = rand_num()
        y = rand_num()
        sign = rand_sign()
        print(f"Question: {x} {sign} {y}")

        if sign == '+':
            correct_answer = x + y
        elif sign == '-':
            correct_answer = x - y
        elif sign == '*':
            correct_answer = x * y

        while True:
            try:
                answer = input("Your answer: ")
                answer = int(answer)
                break
            except ValueError:
                print("Please enter a valid integer.")

        num, continue_game = check_answer(answer, correct_answer, num, name)

        if not continue_game:
            return

    return print(f"Congratulations, {name}!")