# pyp3 시간초과

from sys import stdin
x, y, b = map(int, stdin.readline().split())
time = 0

pmap = sum([list(map(int, stdin.readline().split())) for _ in range(x)], [])

# 블럭 놓기
def put(n:int, low:int):
    global pmap, b, time
    for _ in range(n):
        pmap[pmap.index(low)] += 1
    b -= n
    time += n

# 블럭 캐기
def mine(n:int, high:int):
    global pmap, b, time
    for _ in range(n):
        pmap[pmap.index(high)] -= 1
    b += n
    time += 2 * n

high, low = max(pmap), min(pmap)

if high != low:
    high_count = pmap.count(high)
    low_count = pmap.count(low)
    
    while True:
        if high != low:
            if high_count * 2 > low_count - 1 and b > low_count - 1:
                put(low_count, low)
                low = min(pmap)
                low_count = pmap.count(low)
            else:
                mine(high_count, high)
                high = max(pmap)
                high_count = pmap.count(high)
        else:
            break
    
    print(time, high)
    
else:
    print(time, high)