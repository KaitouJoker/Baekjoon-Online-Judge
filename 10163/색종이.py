from sys import stdin as dn
i      = dn.readline
matrix = [[0] * 1_001 for _ in range(1_001)]
N      = int(i().strip()) + 1
R, E   = range(1, N), [0] * N

def confetti(x1:int, y1:int, x2:int, y2:int, n:int):
    global matrix
    x12, nx2 = x1 + x2, [n] * x2
    for y in range(y1, y1 + y2): matrix[y][x1:x12] = nx2

for j in R: confetti(*map(int, i().split()), j)
for row in matrix:
    for e in row:
        if e: E[e] += 1
print(*E[1:], sep='\n')