from sys import stdin as dn

dn.readline()
original = [*map(int, dn.readline().split())]
counter  = max([original.count(i) for i in original])
B        = original[:]

def swap(a:int, b:int, B:list[int]):
    B[a], B[b] = B[b], B[a]
    return B

def all_swap(b:list[int]):
    global original
    c = [0] * len(b)
    for index_a, i in enumerate(b):
        if i == original[index_a]:
            for index_b, j in enumerate(b):
                if j != i and i != original[index_b] and c[index_a] == 0 and c[index_b] == 0:
                    c[index_a], c[index_b] = b[index_b], b[index_a]
    return b

numbers = {}
for key in original:
    if key in numbers: numbers[key] += 1
    else: numbers[key] = 1

if max([v for v in numbers.values()]) > len(original) // 2: print(-1)
else:
    while True:
        B = all_swap(B)
        for a, b in zip(original, B):
            if a == b: break
        else: break
    print(*B)