w:list[int] = list(map(int, input().split()))
f:list[int] = [1,1,2,2,2,8]
print(*[p - v for v, p in zip(w, f)])