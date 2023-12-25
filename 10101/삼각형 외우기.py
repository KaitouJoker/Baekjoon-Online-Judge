from typing import Callable

p :Callable[..., None] = print
tr:list[int]           = [int(input()) for _ in range(3)]

if   all(i == 60 for i in tr)                  : p('Equilateral')
elif (s:= sum(tr) == 180) and len(set(tr)) == 2: p('Isosceles')
elif s                                         : p('Scalene')
else                                           : p('Error')