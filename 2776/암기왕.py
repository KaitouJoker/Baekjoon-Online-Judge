from typing import Callable

i   :Callable[[str ], str] = input
load:Callable[[None], map] = lambda: map(int, i().split())

for _ in range(T := int(i())):
    i()
    N:set [int] = set(load())
    i()
    M:list[int] = [*load()]
    for m in M: print('01'[m in N])