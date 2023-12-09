from sys import stdin as sin

x, __, block = map(int, sin.readline().split())
pmap = []
for _ in range(x):
    pmap.extend(map(int, sin.readline().split()))
pmap.sort(reverse = True)
time = 128_000_000

def put_dig(height : int):
    global pmap, block
    upper, under = 0, 0
    for b in pmap:
        if b < height:
            under += height - b
        elif b > height:
            upper += b - height
        else:
            continue
    
    if upper + block >= under:
        return upper * 2 + under
    else:
        return False
    

def b_search(heights):
    global time
    if len(heights) <= 1 and time > put_dig(heights[0]):
        return heights[0]
    else:
        middle = heights[len(heights) // 2]
        if (t := put_dig(middle)):
            if t < time:
                time = t
            return b_search(heights[heights.index(middle):])
        else:
            return b_search(heights[:heights.index(middle)])

h = b_search(range(max(pmap), min(pmap) - 1, -1))
print(time, h)
