m, s, m_s = [0] * int(input()), 0, 0
for i in map(int, input().split()):
    i -= 1
    if ~m[i]:
        m[i] = ~m[i]
        s    += 1
    else    : s -= 1
    if m_s < s: m_s = s
print(m_s)