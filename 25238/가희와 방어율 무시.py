from decimal import Decimal as Dm
ERA, ignore = map(Dm, input().split())
if ERA < 100: print(1)
else:
    if ERA * (1 - ignore / 100) < 100: print(1)
    else: print(0)