while (s := input()) != '0':
    n  :int = int(s)
    sum:int = 0
    for i in range(1, n + 1): sum += i
    print(sum)