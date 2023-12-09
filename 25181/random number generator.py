from numpy.random import randint as ri

x = [*ri(1, ri(1, 10), 10)]
print(len(x))
print(*x)