from sys import stdin as dn

k, n = map(int, dn.readline().split())
lans = [int(dn.readline()) for _ in range(k)]
start, end = 1, max(lans)

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in lans:
        lines += i // mid
    
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)