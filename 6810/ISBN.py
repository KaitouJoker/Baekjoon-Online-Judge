from typing import Callable
i:Callable[[], int] = lambda : int(input())
print('The 1-3-sum is', i() + i() * 3 + i() + 91)