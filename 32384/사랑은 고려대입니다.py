from sys import stdin
from typing import Callable

i:Callable = stdin.readline
s:str      = 'LoveisKoreaUniversity'

print(' '.join([s] * int(i())))