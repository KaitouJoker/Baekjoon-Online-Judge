l = list(map(int, (input().split())))
l.remove(max(l))
print(max(l))