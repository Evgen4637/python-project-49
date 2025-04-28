from brain_games.cli import welcome_user
from brain_games.rand import rand_num


def even():
    name = welcome_user()
    print(f'Hello, {name}')
    print('What is the result of the expression?')
    num = 0

    while num < 3:
        x = rand_num()
        y = rand_num()

        print(f"Question: {x} + {y}")
        # summ = random_one

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