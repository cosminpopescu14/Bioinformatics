import random


def adn(n):
    adn = ['a', 'c', 't', 'g']
    return ''. join(random.choice(adn) for x in range(n))
