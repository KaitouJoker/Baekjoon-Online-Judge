def divisor_generator(num:int) -> list[int]:
    return [i for i in range(1, num) if num % i == 0]

while (n:= int(input())) + 1:
    divisor:list[int] = divisor_generator(n)
    if n != sum(divisor): print(n, 'is NOT perfect.')
    else                : print(n, '=', " + ".join(map(str, divisor)))