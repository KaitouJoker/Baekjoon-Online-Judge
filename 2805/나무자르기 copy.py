from sys import stdin as sn

wood  :int       = int(sn.readline().split()[1])
forest:list[int] = sorted(map(int, sn.readline().split()), reverse = True)

def cut(h : int) -> bool:
    global wood, forest
    temp:int = 0
    
    for i in forest:
        if i > h: temp += i - h
        else    : break
        
    if temp >= wood: return True
    else           : return False
    
def b_search(end:int, start:int = 0) -> int:
    while start <= end:
        mid:int = (start + end) // 2

        if cut(mid): start = mid + 1
        else       : end   = mid - 1
    return end

print(b_search(max(forest) + 1))