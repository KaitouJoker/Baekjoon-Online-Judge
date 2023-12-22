from sys import stdin as dn
i = dn.readline
zero_nine:dict[int, list[int]]= {0 : [10],
                                 1 : [1],
                                 2 : [2, 4, 8, 6],
                                 3 : [3, 9, 7, 1],
                                 4 : [4, 6],
                                 5 : [5],
                                 6 : [6],
                                 7 : [7, 9, 3, 1],
                                 8 : [8, 4, 2, 6],
                                 9 : [9, 1]}

for _ in range((int(i().strip()))):
    a, b = map(int, i().split())
    print((x := zero_nine[a % 10])[b % len(x) - 1])