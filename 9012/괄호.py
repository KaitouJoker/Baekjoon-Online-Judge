# for _ in range(int(input())):
#     vps = input()
#     while '()' in vps:
#         vps = vps.replace('()', '')
#     print(['YES', 'NO'][bool(vps)])
    
i = input
def vc(s):
    c = 0
    for b in s:
        c += 1 if b == '(' else -1
        if c < 0: return 'NO'
    if c: return 'NO'
    else: return 'YES'

for _ in range(int(i())):
    print(vc(i()))