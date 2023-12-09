s, n, m = map(int, input().split())
print(abs(x) if (x:= m - s * n) < 0 else 0)