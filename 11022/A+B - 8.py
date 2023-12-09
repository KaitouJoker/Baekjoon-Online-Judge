for i in range(int(input())):
    t = list(map(int, input().split()))
    print("Case #{}: {} + {} = {}".format(i+1, t[0], t[1], sum(t)))