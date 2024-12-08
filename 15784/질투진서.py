N, x, y = map(int, input().split())

maps:list[list[int]] = [list(map(int, input().split())) for _ in range(N)]

jinser = maps[x - 1][y - 1]
line_x = maps[x - 1]
line_y = [row[y - 1] for row in maps]

print('ANGRY' if max(line_x + line_y) > jinser else 'HAPPY')