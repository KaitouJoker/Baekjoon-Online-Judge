print(round(sum(p:=[40 if(n:=int(input()))<40 else n for _ in range(5)])/len(p)))