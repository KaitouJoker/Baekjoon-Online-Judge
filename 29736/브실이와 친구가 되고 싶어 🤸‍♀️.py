p = print
A, B = map(int, input().split())
K, X = map(int, input().split())

if A <= K <= B:
    AB = set(*range(A, B + 1))
    KX = set(*range(K - X, K + X + 1))
    p(len(AB.intersection(KX)))
    
else: p('IMPOSSIBLE')