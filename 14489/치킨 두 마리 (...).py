i = input
c = sum(map(int, i().split()))
h = int(i()) * 2
print(c if c < h else c - h)