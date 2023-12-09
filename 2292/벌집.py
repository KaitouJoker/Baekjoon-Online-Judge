from sys import stdin as dn
n = int(dn.readline().strip())

counter, maps, plus_six = 1, 1, 6
while n > maps:
    counter += 1
    maps += plus_six
    plus_six += 6
print(counter)