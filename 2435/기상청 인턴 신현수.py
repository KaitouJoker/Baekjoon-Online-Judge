import sys
from typing import Callable

input:Callable[[None], str] = sys.stdin.readline

def map_int_split() -> map: return map(int, input().split())

num_count, step  = map_int_split()
nums  :list[int] = [*map_int_split()]
sums  :list[int] = [0]
maxs  :list[int] = []
buffer:int       = 0

for i in range(num_count): sums.append(buffer := buffer + nums[i])

for j in range(step, num_count + 1): maxs.append(sums[j] - sums[j - step])

print(max(maxs))