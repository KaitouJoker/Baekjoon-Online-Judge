from typing import Callable

i:Callable[[], int] = lambda: int(input())

a:int = i()
b:int = i()

print(a + b, a - b, a * b, sep='\n')