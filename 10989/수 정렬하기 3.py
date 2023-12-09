from sys import stdin
nums = [0] * 10_000

for _ in range(int(stdin.readline())):
    nums[int(stdin.readline()) - 1] += 1

for i, j in enumerate(nums):
    if j != 0:
        for _ in range(j):
            print(i + 1)