A, B, C = map(int, input().split())
abc = int(A * B / C)
bca = int(A / B * C)
print(abc if abc > bca else bca)