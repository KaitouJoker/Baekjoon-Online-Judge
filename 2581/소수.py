def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
p = []
for j in range(int(input()), int(input()) + 1):
    if is_prime(j):
        p.append(j)
if p != []:
    print(f'{sum(p)}\n{min(p)}')
else:
    print(-1)