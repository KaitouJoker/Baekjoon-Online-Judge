ab = [*map(int, input().split())]
cd = [*map(int, input().split())]
print(min(ab[0] + cd[1], ab[1] + cd[0]))