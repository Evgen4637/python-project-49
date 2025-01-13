from brain_games.cli import welcome_user
from brain_games.rand import rand_num


def even():
    name = welcome_user()
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num = 0

    while num < 3:
        random_number = rand_num()
        print(f"Question: {random_number}")
        random = random_number % 2
        answer = input("Your answer: ")

        if random != 0:
            if answer == "yes":
                return print(f"'{answer}' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}!") # noqa
            else:
                num += 1
                print("Correct!")

        if random == 0:
            if answer == "yes":
                num += 1
                print("Correct!")
            else:
                return print(f"'{answer}' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}!") # noqa

    return print(f"Congratulations, {name}!")