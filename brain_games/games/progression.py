from brain_games.cli import welcome_user
from brain_games.moduls.rand import rand_num
from brain_games.moduls.utils import check_answer, numerical_answer


def progression():
    name = welcome_user()
    print(f'Hello, {name}')
    print('What number is missing in the progression?')
    num = 0

    while num < 3:
        a1 = rand_num(end=20)
        d = rand_num(end=10)
        n = 10
        progression = [a1 + i * d for i in range(n)]
        hide_index = rand_num(0, n - 1)
        correct_answer = progression[hide_index]
        progression[hide_index] = '..'
        print("Question:", " ".join(str(x) for x in progression))

        answer = numerical_answer()

        num, continue_game = check_answer(answer, correct_answer, num, name)

        if not continue_game:
            return

    return print(f"Congratulations, {name}!")