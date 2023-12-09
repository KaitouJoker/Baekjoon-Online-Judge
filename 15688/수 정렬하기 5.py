import sys
print(*sorted([int(sys.stdin.readline().strip()) for _ in range(int(sys.stdin.readline().strip()))]), sep='\n')