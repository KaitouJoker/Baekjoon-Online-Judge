from typing import Callable

rw:tuple[int]              = range(int(input().split()[0]))
i :Callable[[], list[int]] = lambda : [*map(int, input().split())]

a:list[list[int]] = [i() for _ in rw]
b:list[list[int]] = [i() for _ in rw]
c:list[str]       = [' '.join([str(ai + bi) for ai, bi in zip(ar, br)]) for ar, br in zip(a, b)]

print(*c, sep='\n')

# r=range(int(input().split()[0]));i=lambda:list(map(int,input().split()));print(*[' '.join([str(y+x)for y,x in zip(w,u)])for w,u in zip([i()for _ in r],[i()for _ in r])],sep='\n')