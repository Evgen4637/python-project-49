from random import choice, randint


def rand_num(start=1, end=100):
    return randint(start, end)


def rand_sign():
    return choice(["+", "-", "*"])