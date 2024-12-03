from sys import stdin
from typing import Callable

input:Callable[[None], str] = stdin.readline

def list_int_split() -> list: return list(map(int, input().split()))

number_of_countries, target_country = list_int_split()

medal_list:list[int] = sorted([list_int_split() for _ in range(number_of_countries)], key = lambda x: (x[1], x[2], x[3]), reverse = True)
idx       :int       = [medal_list[i][0] for i in range(number_of_countries)].index(target_country)
rank      :int       = idx

for i in range(number_of_countries):
    if medal_list[idx][1:] == medal_list[i][1:]:
        rank += 1
        break

print(rank)