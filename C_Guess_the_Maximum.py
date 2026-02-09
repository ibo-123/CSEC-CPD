for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        m = min(arr)
        if arr.count(m) == 1 and len(arr) > 1:
                print(m)
        else:
                print(m-1)
                