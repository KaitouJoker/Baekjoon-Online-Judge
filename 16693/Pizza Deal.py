from math import pi
i = input
A1, P1 = map(int, i().split())
R1, P2 = map(int, i().split())
print('Slice of pizza' if A1 / P1 > R1 ** 2 * pi / P2 else 'Whole pizza')