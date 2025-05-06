from brain_games.cli import welcome_user
from brain_games.moduls.rand import rand_num
from brain_games.moduls.utils import affirmative_answer, check_answer


def prime():
    name = welcome_user()
    print(f'Hello, {name}')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    num = 0

    while num < 3:
        a = rand_num()
        print(f"Question: {a}")
        correct_answer = 'no'
        if a == 2:
            correct_answer = 'yes'
        elif a >= 2:
            for i in range(2, int(a ** 0.5) + 1):
                if a % i == 0:
                    break
            else:
                correct_answer = 'yes'

        answer = affirmative_answer()

        num, continue_game = check_answer(answer, correct_answer, num, name)

        if not continue_game:
            return

    return print(f"Congratulations, {name}!")