""" 
i, p = input, print
n    = int(i())

def compare(s1:str, s2:str) -> str:
    return ''.join([i if i == j else '?' for i, j in zip(s1, s2)])

def gen(l1:list[int]) -> str:
    if len(l1) == 1: return l1[0]
    else:
        lf1, lf2, t1, ln = [], [], [], len(l1)
        for idx in range(ln // 2):
            lf1.append(l1[idx * 2])
            lf2.append(l1[idx * 2 + 1])
        
        for j, k in zip(lf1, lf2): t1.append(compare(j, k))
        if ln % 2 == 1: t1.append(l1[-1])
        return gen(t1)

if n == 1: p(i())
else     : p(gen(list(set([i() for _ in range(n)]))))
 """

from sys import stdin as dn

i = dn.readline
item, text = [i().rstrip() for _ in range(int(i()))], ''

for i in zip(*item):
    if len(S:= set(i)) > 1: text += '?'
    else                  : text += list(S)[0]

print(text)