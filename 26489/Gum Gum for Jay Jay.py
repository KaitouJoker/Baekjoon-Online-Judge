c = 0
while True:
    try:
        input()
        c += 1
    except EOFError: break
print(c)