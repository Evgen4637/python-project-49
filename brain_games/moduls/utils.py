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