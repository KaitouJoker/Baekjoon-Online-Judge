if len(AB:=input()) == 2 or (len(AB) == 3 and AB[2] == '0'): x = int(AB[:1]) + int(AB[1:])
else: x = int(AB[:2]) + int(AB[2:])
print(x)