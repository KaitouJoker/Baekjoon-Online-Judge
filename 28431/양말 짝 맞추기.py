s = [0] * 10
for _ in range(5): s[index] = not(s[index:=int(input())])
for e, s in enumerate(s):
    if s: print(e)