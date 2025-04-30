import random

def rand_num(start=1, end=100):
    return random.randint(start, end)

def rand_sign():
    return random.choice(["+", "-", "*"])