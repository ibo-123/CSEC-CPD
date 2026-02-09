for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        x = int(input())
        truth = False
        min_ = min(arr)
        max_ = max(arr)
        if x >= min_ and x <= max_:
                print("YES")
        else:
                print("NO")
        