T = int(input())

a:int = 300
b:int = 60
c:int = 10

A:int = T // a
B:int = T % a // b
C:int = T % b // c

if T % c > 0: print(-1)
else: print(A, B, C)