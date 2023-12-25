from typing import Callable

isp:Callable[[], list[int]] = lambda : [*map(int, input().split())]
p  :Callable[..., None]     = print

year    , month    , day     = isp()
now_year, now_month, now_day = isp()

over_month_day:bool = [month, day] > [now_month, now_day]
ny            :int  = now_year - year

p(ny - over_month_day)
p(ny + 1)
p(ny)