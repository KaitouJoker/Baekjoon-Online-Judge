# pyp3 통과함

from sys import stdin as sin

def put_dig(height : int, map : list[int]):
    upper, under = 0, 0
    for p in map:
        if p < height:
            under += height - p
        else:
            upper += p - height
    return [height, upper, under]

x, y, block = map(int, sin.readline().split())
pmap = []
for _ in range(x):
    pmap.extend(map(int, sin.readline().split()))

time = 128_000_000
for height, upper, under in [put_dig(base, pmap) for base in range(max(pmap), min(pmap) - 1, -1)]:
    if time > (New_time := upper * 2 + under):
        if under < upper + block + 1:
            time, h = New_time, height
    else:
        if under < upper + block + 1:
            break

print(time, h)