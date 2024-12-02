import sys

def map_int_split() -> map: return map(int, sys.stdin.readline().split())

num, sum_count = map_int_split()

nums:list[int] = [*map_int_split()]
sums:list[int] = [0]
buffer:int = 0

for i in range(num): sums.append(buffer := buffer + nums[i])

for _ in range(sum_count):
    i, j = map_int_split()
    print(sums[j] - sums[i - 1])