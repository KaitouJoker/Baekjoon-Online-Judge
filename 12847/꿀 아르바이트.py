import sys
from typing import Callable

def map_int_split() -> map: return map(int, sys.stdin.readline().split())

input:Callable[[None], str] = sys.stdin.readline

work_day, work = map_int_split()

days         :list[int] = [*map_int_split()]
buffer       :int       = sum(days[:work])
maximum_value:int       = sum(days[:work])
    
for i in range(work_day - work):
    buffer -= days[i]
    buffer += days[i + work]
    maximum_value = max(maximum_value, buffer)

print(maximum_value)