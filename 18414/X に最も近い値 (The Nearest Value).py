X, L, R = map(int, input().split())
case = [*range(L, R + 1)]

def f(n, x):
    if n > x: return abs(n - x)
    else: return abs(x - n)

c, index = f(case[0], X), 0
for i, n in enumerate(case[1:], 1):
    if c > (v := f(n, X)): c, index = v, i
    
print(case[index])