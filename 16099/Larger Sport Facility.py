i = input
for _ in range(int(i())):
    lt, wt, le, we = map(int, i().split())
    t, e = lt * wt, le * we
    print('TelecomParisTech' if t > e else 'Eurecom' if t < e else 'Tie')