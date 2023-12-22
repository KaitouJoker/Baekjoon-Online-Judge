height:int = 0
c     :int = 0
for bowl in input():
    if c > 0:
        if bowl != last_bowl: height += 10
        else: height += 5
    else:
        c += 1
        height += 10
    last_bowl = bowl
print(height)