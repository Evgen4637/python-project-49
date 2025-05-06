from brain_games.cli import welcome_user
from brain_games.moduls.rand import rand_num
from brain_games.moduls.utils import check_answer


def even():
    name = welcome_user()
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num = 0

    while num < 3:
        random_number = rand_num()
        print(f"Question: {random_number}")
        is_even = random_number % 2 == 0
        correct_answer = "yes" if is_even else "no"
        answer = input("Your answer: ")
        while answer not in ["yes", "no"]:
            print("Please answer 'yes' or 'no'.")
            answer = input("Your answer: ")

        num, continue_game = check_answer(answer, correct_answer, num, name)

        if not continue_game:
            return

    return print(f"Congratulations, {name}!")