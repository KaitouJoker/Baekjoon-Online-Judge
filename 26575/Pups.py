i = input
for _ in range(int(i())):
    d, f, p = map(float, i().split())
    print(f'${d * f * p:.2f}')