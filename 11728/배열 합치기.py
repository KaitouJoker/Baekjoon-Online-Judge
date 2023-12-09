import sys;sys.stdin.readline().split()
print(*sorted([int(i)for _ in range(2)for i in sys.stdin.readline().split()]),sep=' ')