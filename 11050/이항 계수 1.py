pt = [[1], [1, 1]]
N, K = map(int, input().split())
for _ in range(N - 1):
    l = [1]
    for j in range(len(pt[-1]) - 1): l += [pt[-1][j] + pt[-1][j + 1]]
    l += [1]
    pt += [l]
print(pt[N][K])
# --------------------------------
from math import factorial as fc
N, K = map(int, input().split())
print(int(fc(N) / (fc(K) * fc(N - K))))