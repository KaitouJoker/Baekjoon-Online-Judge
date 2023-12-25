from typing import Callable

p  :Callable[..., None] = print
la :list[int]           = sum([list(map(int, input().split())) for _ in range(9)], [])
ma :int                 = max(la)
mai:int                 = la.index(ma)

p(ma)
p((mai) // 9 + 1, (mai) % 9 + 1)