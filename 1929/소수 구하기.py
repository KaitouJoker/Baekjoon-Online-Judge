from sys import stdin as sd

def isPrime(n : int):
    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            break
    else:
        if n != 1:
            print(n)

s, e = map(int, sd.readline().split())
for i in range(s, e + 1):
    isPrime(i)