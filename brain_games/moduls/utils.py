def check_answer(answer, correct_answer, num, name):
    if answer == correct_answer:
        num += 1
        print("Correct!")
        return num, True
    else:
        print(
            f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"  # noqa
            f"Let's try again, {name}!")
        return num, False


def numerical_answer():
    while True:
        try:
            answer = input("Your answer: ")
            answer = int(answer)
            return answer
        except ValueError:
            print("Please enter a valid integer.")


def affirmative_answer():
    answer = input("Your answer: ")
    while answer not in ["yes", "no"]:
        print("Please answer 'yes' or 'no'.")
        answer = input("Your answer: ")
    return answer