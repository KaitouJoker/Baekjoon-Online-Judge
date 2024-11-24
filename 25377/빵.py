case = [list(map(int, input().split())) for _ in range(int(input()))]
can = [[a, b] for a, b in case if a <= b]
if can != []: print(min(can, key=lambda x: x[1])[1])
else: print(-1)