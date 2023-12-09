hour, minutes = map(int, input().split())
add_time =  int(input())

hour += add_time // 60
minutes += add_time % 60

if minutes > 59:
    hour += 1
    minutes -= 60
    
if hour > 23:
    hour -= 24

print(f'{hour} {minutes}')