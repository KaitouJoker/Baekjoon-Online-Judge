start, end = sorted([*map(int, input().split())])
num:list[int] = [i for i in range(start + 1, end)]
print(len(num))
print(*num)