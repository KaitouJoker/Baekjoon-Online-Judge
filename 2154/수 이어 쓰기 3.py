N:str = input()
s:str = ''.join(map(str, [*range(1, int(N) + 1)]))
print(s.find(N) + 1)