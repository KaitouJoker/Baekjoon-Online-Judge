i = lambda x, y: 'Yes' if x > y else 'No'
while 1:
    a, b = map(int, input().split())
    
    if a == 0: break
    else     : print(i(a, b))