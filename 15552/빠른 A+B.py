from sys import stdin as sn

for i in range(int(input())):
    t = list(map(int, sn.readline().split()))
    print(sum(t))