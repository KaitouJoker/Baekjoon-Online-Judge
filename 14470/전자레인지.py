i = input
A, B, C, D, E = int(i()), int(i()), int(i()), int(i()), int(i())
time = 0
if A < 0:
    time += abs(A) * C
    A = 0
if A == 0: time += D
time += E * (B - A)
print(time)