from sys import stdin as dn
def hashing(plus):
    return ((ord(plus[1]) - 96) * pow(31, plus[0])) % 1234567891

_, word = int(dn.readline().rstrip()), dn.readline().rstrip()
print(sum(map(hashing, enumerate(word))) % 1234567891)