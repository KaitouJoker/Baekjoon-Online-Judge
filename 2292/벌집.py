from sys import stdin as dn
n:int = int(dn.readline().strip())

counter :int = 1
maps    :int = 1
plus_six:int = 6

while n > maps:
    counter  += 1
    maps     += plus_six
    plus_six += 6
print(counter)