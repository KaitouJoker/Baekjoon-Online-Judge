numbers:list[int] = list(map(int, input().split()))
num_set:set[int]  = set(numbers)
temp_l1:list[int] = [i for i in num_set if numbers.count(i) == 2]

if   len(num_set) == 3: print(max(num_set) * 100)
elif len(num_set) == 1: print(10_000 + numbers[0] * 1_000)
else                  : print(1_000 + temp_l1[0] * 100)