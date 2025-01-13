from brain_games.cli import welcome_user
from brain_games.greetings import greet


def main():

    greet()

    print('Hello, ' + welcome_user())


if __name__ == "__main__":
    main()
