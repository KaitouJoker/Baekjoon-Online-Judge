i, p = input, print
X = lambda n: '0' * (2 - len(n)) + n
md = int(X(i()) + X(i()))
if md > 218: p('After')
elif md < 218: p('Before')
else: p('Special')