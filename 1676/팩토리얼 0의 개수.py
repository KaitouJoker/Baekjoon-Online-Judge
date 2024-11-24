import math
F,c=list(str(math.factorial(int(input())))),0
for n in F[::-1]:
    if n=='0':c+=1
    else:break
print(c)