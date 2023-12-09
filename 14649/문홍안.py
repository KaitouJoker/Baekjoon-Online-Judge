p              = print
asset          = int(input())
stepping_stone = ['b'] * 100

def swap(rgb:str):
    if rgb == 'b'  : return 'r'
    elif rgb == 'r': return 'g'
    else           : return 'b'

def run(n:int, direction:str):
    global stepping_stone
    if direction == 'L': stepping_stone[:n-1] = map(swap, stepping_stone[:n-1])
    else               : stepping_stone[n:]   = map(swap, stepping_stone[n:])

def count(asset:int, stone:list[str], x:str) -> str:
    return f'{asset * stone.count(x) / 100:.2f}'

for _ in range(int(input())):
    n, direction = input().split()
    run(int(n), direction)

for c in 'brg': p(count(asset, stepping_stone, c))