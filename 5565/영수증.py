from typing import Callable
i:Callable[[], str] = input
N:int               = int(i())
for _ in range(9): N -= int(i())
print(N)