i = lambda: list(map(int, input().split()))
s = lambda data: sum(get * point for get, point in zip(data, [6, 3, 2, 1, 2]))
print(s(i()), s(i()))