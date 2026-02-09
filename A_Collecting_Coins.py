for i in range(int(input())):
        a,b,c,n = map(int, input().split())
        max_ = max(a,b,c)
        total = (max_ - a) + (max_ - b) + (max_ - c)
        n -= total
        if n >= 0 and n%3==0:
                print("YES")
        else:
                print("NO")