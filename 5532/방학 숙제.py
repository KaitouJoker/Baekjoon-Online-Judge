L, A, B, C, D = [int(input()) for _ in range(5)]
AC:int = A // C
BD:int = B // D
if A % C: AC += 1
if B % D: BD += 1
print(L - max(AC, BD))