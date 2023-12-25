from typing import Callable

i:Callable[[int, int], str] = lambda x, y: 'Yes' if x > y else 'No'

while 1:
    a, b = map(int, input().split())
    
    if a: print(i(a, b))
    else: break