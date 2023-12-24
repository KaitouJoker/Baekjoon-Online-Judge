from typing import Final
cmd:Final = {'@' : lambda x : x * 3,
             '%' : lambda x : x + 5,
             '#' : lambda x : x - 7}
for _ in range(int(input())):
    n, *cm = input().split()
    n:float = float(n)
    for c in cm: n = cmd[c](n)
    print(f'{n:.2f}')