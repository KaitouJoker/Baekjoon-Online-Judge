from sys import stdin as dn

k, n = map(int, dn.readline().split())
lans  :list[int] = [int(dn.readline()) for _ in range(k)]
start :int       = 1
end   :int       = max(lans)

while start <= end:
    mid  :int = (start + end) // 2
    lines:int = 0
    for i in lans: lines += i // mid
    
    if lines >= n: start = mid + 1
    else         : end   = mid - 1

print(end)