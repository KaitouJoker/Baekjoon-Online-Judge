input()
c = 0
for p in input():
    if p == 'A': c += 1
    else: c -= 1
print('A' if c > 0 else 'B' if c < 0 else 'Tie')