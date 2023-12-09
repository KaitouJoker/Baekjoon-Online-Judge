t = []
t.append(input())
t.append(input())

for i in list(t[1]):
    t.append(int(t[0]) * int(i))

print("{}\n{}\n{}\n{}".format(t[4], t[3], t[2], int(t[1]) * int(t[0])))