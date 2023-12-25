from typing import Callable
i:Callable[[], int] = lambda: int(input())
Y:int = i()
M:int = i()
print(M * 2 - Y)