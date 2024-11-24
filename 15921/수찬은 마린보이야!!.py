i, p = input, print
N = int(i())
if N == 0: p('divide by zero')
else:
    avg = 0
    px = 0
    r = [0] * 101
    for point in map(int, i().split()): r[point] += 1
    for idx, count in enumerate(r):
        if count > 0:
            px  += idx * count / N
            avg += idx * count
    p(f'{(avg / N) / px:.2f}')

""" 
print('divide by zero' if int(input()) == 0 else '1.00')
 """