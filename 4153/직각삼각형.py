from sys import stdin as dn

def pytha(abc:list[int]):
    c = abc.pop(abc.index(max(abc)))
    a, b = abc
    if pow(a, 2) + pow(b, 2) == pow(c, 2):
        return 'right'
    else: return 'wrong'

while 1:
    abc = list(map(int, dn.readline().split()))
    if sum(abc) == 0:
        break
    else:
        print(pytha(abc))

""" 
from sys import stdin
while 1:
    if sum(l:=list(map(lambda x:int(x)**2,stdin.readline().split())))==0:break
    else:print('right'if l.pop(l.index(max(l)))==l[0]+l[1] else 'wrong')
 """