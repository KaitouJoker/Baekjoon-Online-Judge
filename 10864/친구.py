n, m = map(int, input().split())
l1 = []

for i in range(m):
    a, b = map(int, input().split())
    
    l1.append(a)
    l1.append(b)

for i in range(1, n + 1): print(l1.count(i))