from sys import stdin as sn
wood = int(sn.readline().split()[1])
forest = sorted(map(int, sn.readline().split()), reverse = True)

def cut(h : int):
    global wood, forest
    temp = 0
    for i in forest:
        if i > h:
            temp += i - h
        else:
            break
        
    if temp >= wood:
        return True
    else:
        return False
    
def b_search(end:int, start=0):
    while start <= end:
        mid = (start + end) // 2

        if cut(mid):
            start = mid + 1
        else:
            end = mid - 1
    
    return end

print(b_search(max(forest) + 1))