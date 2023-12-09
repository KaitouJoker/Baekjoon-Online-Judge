from sys import stdin as dn
q = int(dn.readline().split()[1])
seq = list(map(int, dn.readline().split()))

def one(arg:list[int]):
    global seq
    result = sum(seq[arg[0] - 1 : arg[1]])
    seq[arg[0] - 1], seq[arg[1] - 1] = seq[arg[1] - 1], seq[arg[0] - 1]
    return result

def two(arg:list[int]):
    global seq
    ab = sum(seq[arg[0] - 1 : arg[1]])
    cd = sum(seq[arg[2] - 1 : arg[3]])
    return ab - cd

command = [one, two]
for _ in range(q):
    c, *nums = map(int, input().split())
    print(command[c - 1](nums))