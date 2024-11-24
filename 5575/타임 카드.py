a = [(T1 := [*map(int, input().split())])[:3], T1[3:]]
b = [(T2 := [*map(int, input().split())])[:3], T2[3:]]
c = [(T3 := [*map(int, input().split())])[:3], T3[3:]]
abc = [a, b, c]

def time2sec(Tn:list[int]) -> int:
    h, m, s = Tn[0] * 3600, Tn[1] * 60, Tn[2]
    return h + m + s

def sec2time(sec:int) -> list[int]:
    h, m, s = sec // 3600, (sec % 3600) // 60, sec % 60
    return [h, m, s]

for start, end in abc:
    check = time2sec(start)
    out   = time2sec(end)
    print(*sec2time(out - check), sep = ' ')