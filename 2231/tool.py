def calc(n:int):
    x = n + sum(map(int, list(str(n))))
    return [n / x, n, x]

rs = sorted([calc(i) for i in range(100000, 1000000)], key = lambda x : x[0])
print(*rs[0])