T = int(input())
a, b, c = 300, 60, 10
A, B, C = T // a, T % a // b, T % b // c

if T % c > 0: print(-1)
else: print(A, B, C)