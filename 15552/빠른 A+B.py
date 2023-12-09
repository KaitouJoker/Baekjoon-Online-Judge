import sys

for i in range(int(input())):
    t = list(map(int, sys.stdin.readline().split()))
    print(sum(t))