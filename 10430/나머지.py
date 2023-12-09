t = input().split()
for i in t:
    t[t.index(i)] = int(i)

A, B, C = t[0], t[1], t[2]

print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)