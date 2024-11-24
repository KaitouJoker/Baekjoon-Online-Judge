N, W, H, L = map(int, input().split())
print(i if (i := (W // L) * (H // L)) < N else N)