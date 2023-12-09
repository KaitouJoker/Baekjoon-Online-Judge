a = {f'{i}':0 for i in 'abcdefghijklmnopqrstuvwxyz'}
for j in input(): a[j] += 1
print(*[k for k in a.values()])