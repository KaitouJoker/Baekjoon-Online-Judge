t:list[int] = [*map(int, [input(), input()])]

for i in str(t[1]): t.append(t[0] * int(i))

print(t[4], t[3], t[2], t[1] * t[0], sep = '\n')