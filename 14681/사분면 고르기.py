t = []
t.append(int(input()))
t.append(int(input()))
#t = list(map(float, t))

if t[0] > 0:
    if t[1] > 0: print(1)
    else       : print(4)
else:
    if t[1] > 0: print(2)
    else       : print(3)