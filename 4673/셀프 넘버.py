from typing import Callable

d:Callable[[int], int] = lambda n : n + sum(map(int, list(str(n))))

a:set[int] = {*range(1, 10_001)}
x:set[int] = {d(i) for i in range(1, 10_001)}

print(*sorted(a - x), sep='\n')

""" 
d=lambda n:n+sum(list(map(int,list(str(n)))))
print(*sorted({*range(1,10001)}-{d(i)for i in range(1,10001)}),sep='\n')
 """