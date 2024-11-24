dial = {'ABC'  : 3,
        'DEF'  : 4,
        'GHI'  : 5,
        'JKL'  : 6,
        'MNO'  : 7,
        'PQRS' : 8,
        'TUV'  : 9,
        'WXYZ' : 10}

c = 0
for n in input():
    for k, v in dial.items():
        if n in k:
            c += v
            break

print(c)