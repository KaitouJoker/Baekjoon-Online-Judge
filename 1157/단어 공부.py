s = input().upper()
tables = list(set(s))
counter = [s.count(i) for i in tables]

if len([j for j in counter if j == max(counter)]) > 1:
    print('?')
else:
    print(tables[counter.index(max(counter))])