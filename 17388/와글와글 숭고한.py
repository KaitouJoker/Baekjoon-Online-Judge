from typing import Final

p    :Final     = print
skh  :list[str] = ['Soongsil', 'Korea', 'Hanyang']
point:list[int] = [*map(int, input().split())]

if sum(point) >= 100: p('OK')
else                : p(skh[point.index(min(point))])