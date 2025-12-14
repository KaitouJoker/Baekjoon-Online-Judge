from sys import stdin as dn
from typing import Callable
i:Callable = dn.readline

curriculum:dict[str,str] = {
    'F' : 'Foundation',
    'C' : 'Claves',
    'V' : 'Veritas',
    'E' : 'Exploration'}

print(curriculum[i().strip()[0]])