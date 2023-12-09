from sys import stdin as dn
print(*map(lambda x:f'{x[0]} {x[1]}',sorted([list(map(int,dn.readline().split()))for _ in range(int(dn.readline().strip()))],key=lambda x:(x[1],x[0]))),sep='\n')