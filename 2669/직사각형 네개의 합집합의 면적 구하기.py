from sys import stdin
i = stdin.readline

page:list[list[int]] = [[0] * 101 for _ in range(101)]

def confetti(x1:int, y1:int, x2:int, y2:int):
    global page
    line_x, line_y = x2 - x1, y2 - y1
    
    for y in range(y1, y1 + line_y): page[y][x1:x1 + line_x] = [1] * (line_x)

for _ in range(4): confetti(*map(int, i().split()))
    
print(sum(sum(page, [])))