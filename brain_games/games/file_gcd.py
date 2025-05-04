import math

from brain_games.cli import welcome_user
from brain_games.moduls.rand import rand_num
from brain_games.moduls.utils import check_answer


def gcd():
    name = welcome_user()
    print(f'Hello, {name}')
    print('Find the greatest common divisor of given numbers.')
    num = 0

    while num < 3:
        x = rand_num()
        y = rand_num()
        print(f"Question: {x} {y}")
        correct_answer = math.gcd(x, y)

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