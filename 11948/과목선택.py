A = sorted([int(input()) for _ in range(4)], reverse=True)
B = max(int(input()) for _ in range(2))
print(sum(A[:3]) + B)