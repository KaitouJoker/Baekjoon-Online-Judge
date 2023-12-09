N = int(input())
c = 0
TSN = 3
while TSN <= N:
    c += (S:=str(TSN)).count('3') + S.count('6') + S.count('9')
    TSN += 1
print(c)