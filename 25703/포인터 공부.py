p = print
N = int(input())
ptr = 'a'
p(f'int {ptr};')
for i in range(1, N + 1):
    p(f"int {'*' * i}ptr{'' if i < 2 else i} = &{'ptr{}'.format('' if ptr < 2 else ptr) if ptr != 'a' else ptr};")
    ptr = i