from sys import stdin as dn
i = dn.readline
page = [[0] * 100 for _ in range(100)]

def confetti(x1:int, y1:int):
    global page
    x10, one_10 = x1 + 10, [1] * 10
    for y in range(y1, y1 + 10): page[y][x1:x10] = one_10

for _ in range(int(i().strip())): confetti(*map(int, i().split()))
page = [e for ee in page for e in ee if e == 1]
print(len(page))