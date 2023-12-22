from sys import stdin

stack = []

def push(n):
    global stack
    stack.append(n[0])

size  = lambda x = None : len(stack)
empty = lambda x = None : 1 if len(stack) == 0 else 0
top   = lambda x = None : -1 if len(stack) == 0 else stack[-1]

def pop(x = None):
    global stack
    if empty(x):
        return -1
    else:
        return stack.pop()

for i in range(int(input())):
    command, *data = stdin.readline().split()
    
    if (r := globals()[command](data)) != None:
        print(r)