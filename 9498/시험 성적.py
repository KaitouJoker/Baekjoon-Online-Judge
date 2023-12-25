from typing import Callable
p:Callable[..., None] = print
t:int = int(input())

if   t >= 90: p("A")
elif t >= 80: p("B")
elif t >= 70: p("C")
elif t >= 60: p("D")
else        : p("F")