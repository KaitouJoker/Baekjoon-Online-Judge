start, end = map(int, input().split())
arr:list[int] = []
c  :int       = 1
cc :int       = 1
for _ in range(end):
    if cc == 0:
        c += 1
        cc = c
    arr.append(c)
    cc -= 1

print(sum(arr[start - 1: end]))