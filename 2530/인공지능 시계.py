h, m, s, t = map(int, input().split() + [input()])

h += t // 3_600
m += t % 3_600 // 60
s += t % 60

if s > 59:
    s -= 60
    m += 1
if m > 59:
    m -= 60
    h += 1
if h > 23: h %= 24

print(h, m, s)