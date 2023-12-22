def is_prime(n: int):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
input()
l, c = list(map(int, input().split())), 0
for i in l:
    if is_prime(i):
        c += 1
print(c)