from sys import stdin as sn

re = lambda i : i + sum(map(int, list(str(i))))

def space(n : int) -> int:
    if   n < 19     : return int(n * 1 / 2)
    elif n < 199    : return int(n * 19 / 29)
    elif n < 1_099  : return int(n * 199 / 218)
    elif n < 10_999 : return int(n * 1_099 / 1_118)
    elif n < 109_999: return int(n * 10_999 / 11_027)
    else            : return int(n * 109_999 / 110_036)

n  :str = sn.readline().rstrip()
i_n:int = int(n)

for i in range(space(i_n), i_n):
    if re(i) == i_n:
        print(i)
        break
else:print(0)
    
""" 
import sys;r=lambda i:i+sum(map(int,list(str(i))));p=print
def s(n):return int(n*(1/2 if n<19 else 19/29 if n<199 else 199/218 if n<1099 else 1099/1118 if n<10999 else 10999/11027 if n<109999 else 109999/110036))
n=sys.stdin.readline().rstrip();u=int(n)
for i in range(s(u),u):
    if r(i)==u:
        p(i)
        break
else:p(0)
 """