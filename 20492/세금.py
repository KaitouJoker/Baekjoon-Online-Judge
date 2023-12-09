N = int(input())
key = lambda x: x * 78 / 100
print(round(key(N)), round(N * 0.8 + key(N * 0.2)))