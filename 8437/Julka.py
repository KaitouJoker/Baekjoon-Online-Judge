from typing import Callable
inp:Callable[[], int] = lambda: int(input())

apple:int = inp()
d    :int = inp() // 2 * 2
Ea   :float = apple % 2

apple -= Ea

Kla:int = (Fa:=apple // 2) + (Point:=d // 2) + Ea
Nat:int = Fa - Point

print(Kla, Nat, sep='\n')