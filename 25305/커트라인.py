count = int(input().split()[1]) - 1

print(sorted(map(int, input().split()), reverse=True)[count])