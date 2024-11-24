from typing import Callable

AB:list[int] = [0, 0]

get_AB:Callable[[None], list[int]] = lambda : [*map(int, input().split())]

for _ in range(int(input())):
    ab:list[int] = get_AB()
    if ab[0] == ab[1]: continue
    AB[ab[0] < ab[1]] += 1

print(*AB)