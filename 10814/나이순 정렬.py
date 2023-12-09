from sys import stdin as dn
k = lambda x: x[0]
i = lambda x: [int(x[0]), x[1]]
s = lambda x: ' '.join([str(x[0]), x[1]])

r = range(int(dn.readline().rstrip()))
x = [dn.readline().split() for _ in r]
y = sorted(map(i, x), key=k)
z = list(map(s, y))
print(*z, sep='\n')