n = int(input())
seq = list(map(int,input().split()))
si = sorted([x, i] for i, x in enumerate(seq))
ti = si[:]
while any(i[0] == j[0] for i, j in zip(si, ti)):
    ti.append(ti.pop(0))
    if ti == si:
        print(-1)
        break
else:
    tit = [[t[0], s[1]] for s, t in zip(si, ti)]
    teq = [k[0] for k in sorted(tit, key=lambda x: x[1])]
    print(*teq)
