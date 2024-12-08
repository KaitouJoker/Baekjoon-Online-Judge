x:list[int] = []
y:list[int] = []

for _ in '123':
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for xi, yi in zip(x, y):
    if x.count(xi) < 2: xn:int = xi
    if y.count(yi) < 2: yn:int = yi

print(xn, yn)