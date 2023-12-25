from typing import Callable
p:Callable[[], str] = input
S:int               = sum(map(int, input().split()))
T:int               = sum(map(int, input().split()))
if S > T: p(S)
else: p(T)