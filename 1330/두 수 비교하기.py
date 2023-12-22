to:list[str] = input().split()
t :list[int] = list(map(int, to))

if   t[0] == t[1]: print("==")
elif t[0] <  t[1]: print("<")
else             : print(">")