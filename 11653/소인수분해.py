n = int(input())
d = 2
while n >= d:
    if n % d == 0:
        print(d)
        n = n / d
    else:
        d = d + 1