from sys import stdin as dn
key = lambda x: (x[0], x[1])
xy = sorted([list(map(int,dn.readline().split())) for _ in range(int(dn.readline().strip()))], key = key)
for x, y in xy:
    print(f'{x} {y}')

""" 
from sys import stdin as dn
print(*map(lambda x:f'{x[0]} {x[1]}',sorted([list(map(int,dn.readline().split()))for _ in range(int(dn.readline().strip()))],key=lambda x:(x[0],x[1]))),sep='\n')
 """