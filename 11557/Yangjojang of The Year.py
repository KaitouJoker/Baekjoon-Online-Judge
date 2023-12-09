i = lambda x, y: [x, int(y)]
for _ in range(int(input())):
    u, a = [], []
    for _ in range(int(input())):
        ui, ai = input().split()
        u.append(ui)
        a.append(int(ai))
    print(u[a.index(max(a))])