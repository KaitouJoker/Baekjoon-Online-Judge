a={*range(1,31)}
b={int(input())for i in range(28)}
print(*sorted(a-b),sep='\n')

# print(*sorted({*range(1,31)}-{int(input())for i in range(28)}),sep='\n')