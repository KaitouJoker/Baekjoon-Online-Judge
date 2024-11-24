
def swap(Q:list[int], a:int, b:int) -> list:
    A:int = Q[a]
    B:int = Q[b]
    Q[a:b + 1] = [B, A]
    return Q

Q:list[int] = [*map(int, input().split())]
A:list[int] = [*range(1, len(Q) + 1)]
C:     int  = 0
while Q != A:
    for i in range(1, len(Q)):
        if Q[i - 1] > Q[i]:
            Q = swap(Q, i - 1, i)
            C += 1
            print(*Q)

print(C)