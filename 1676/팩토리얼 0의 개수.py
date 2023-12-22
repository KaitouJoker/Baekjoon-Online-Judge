import math
F:list[str] = list(str(math.factorial(int(input()))))
c:int       = 0
for n in F[::-1]:
    if n == '0': c += 1
    else       : break
print(c)