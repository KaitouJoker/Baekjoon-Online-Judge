F, n = [0, 1], int(input())
for _ in range(n - 1): F += [F[-1] + F[-2]]
print(F[n])