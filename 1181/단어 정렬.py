from sys import stdin
d=stdin.readline

word_list = sorted(set([d().rstrip() for _ in range(int(d().rstrip()))]), key = lambda x : (len(x), x))

print(*word_list, sep='\n')

""" from sys import stdin
d=stdin.readline
print(*sorted(set([d().rstrip()for _ in range(int(d().rstrip()))]),key=lambda x:(len(x),x)),sep='\n')
 """