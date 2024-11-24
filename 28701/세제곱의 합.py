from math import pow

N1 = (N:=int(input())) * (N + 1) // 2
N2 = round(pow(N1, 2))
N3 = round(sum([pow(i, 3) for i in range(2, N + 1)], 1))

print(N1, N2, N3, sep='\n')