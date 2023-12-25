a:set[int] = {*range(1,31)}
b:set[int] = {int(input()) for _ in range(28)}
print(*sorted(a - b), sep = '\n')

# print(*sorted({*range(1,31)}-{int(input())for i in range(28)}),sep='\n')