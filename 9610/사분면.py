Q1  :int = 0
Q2  :int = 0
Q3  :int = 0
Q4  :int = 0
AXIS:int = 0

for _ in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0: AXIS += 1
    else:
        if x > 0:
            if y > 0: Q1 += 1
            else    : Q4 += 1
        else:
            if y > 0: Q2 += 1
            else    : Q3 += 1

print(f'Q1: {Q1}',
      f'Q2: {Q2}',
      f'Q3: {Q3}',
      f'Q4: {Q4}',
      f'AXIS: {AXIS}',
      sep='\n')