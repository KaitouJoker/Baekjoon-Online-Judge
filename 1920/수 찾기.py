from sys import stdin as dn
d = dn.readline
d()
A:set[int] = set(map(int, d().split()))
d()
for i in map(int, d().split()): print(1 if i in A else 0)