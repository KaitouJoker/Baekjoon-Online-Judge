start, end = map(int, input().split())
arr = []
c = 1
cc = c
for _ in range(end):
    if cc == 0:
        c += 1
        cc = c
    arr.append(c)
    cc -= 1

print(sum(arr[start - 1: end]))