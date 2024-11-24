t = input().split()
t = list(map(int, t))

if t[0] == t[1]:
    print("==")
elif t[0] < t[1]:
    print("<")
else:
    print(">")