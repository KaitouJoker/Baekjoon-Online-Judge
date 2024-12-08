win  :int = 0
score:int = 0

for index, scoreboard in enumerate([map(int, input().split()) for _ in range(5)], 1):
    if (calc:=sum(scoreboard)) > score:
        win   = index
        score = calc

print(win, score)