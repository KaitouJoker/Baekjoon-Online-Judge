def bs(n:int):
    start:int = 1
    end  :int = n
    
    while start <= end:
        p:int = (start + end) // 2
        if   (c := p * (p + 1) / 2) == n: return p
        elif c < n                      : start = p + 1
        else                            : end   = p - 1
    return end
    
print(bs(int(input())))