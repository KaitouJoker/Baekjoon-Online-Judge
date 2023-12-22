import sys
from itertools import combinations as cb
i:list[int] = [int(sys.stdin.readline().strip()) for _ in range(9)]
x = [*cb(i, 7)]
for c in x:
    if sum(c) == 100:
        print(*sorted(c), sep='\n')
        break
    
""" 
from itertools import *
for c in [*combinations([int(input())for _ in range(9)],7)]:
    if sum(c)==100:print(*sorted(c),sep='\n');break
 """