from typing import Callable

def is_prime(n:int):
    if n == 1: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

i:Callable[[], int] = lambda: int(input())
p:list[int]         = [j for j in range(i(), i() + 1) if is_prime(j)]

if p: print(sum(p), min(p), sep = '\n')
else: print(-1)