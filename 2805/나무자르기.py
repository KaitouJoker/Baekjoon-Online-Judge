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
    
def b_search(heights):
    if len(heights) <= 1:
        return heights[0]
    else:
        middle = heights[len(heights) // 2]
        if cut(middle):
            return b_search(heights[heights.index(middle):])
        else:
            return b_search(heights[:heights.index(middle)])

print(b_search(range(max(forest) + 1)))