while 1:
    b = input()
    if b == '0':
        break
    else:
        if b == b[::-1]:
            print('yes')
        else:
            print('no')