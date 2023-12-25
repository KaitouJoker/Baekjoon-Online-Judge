from typing import Callable
i:Callable[[], str] = input
print(eval(i() + i() + i()))