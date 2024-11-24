hour, sake = map(int, input().split())
if sake or not(11 < hour < 17): print(280)
else                          : print(320)