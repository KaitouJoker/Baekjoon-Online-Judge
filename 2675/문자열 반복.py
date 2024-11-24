for i in range(int(input())):
    n, s = input().split()
    r = ''
    for l in s:
        r += l * int(n)
    print(r)