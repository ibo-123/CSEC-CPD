for i in range(int(input())):
        n , m = map(int,input().split())
        arr = list(map(int,input().split()))
        truth = False
        arr.sort()
        l , r = 0 , n-1
        while l < r:
                if arr[l]+arr[r] >= m and arr[l]+arr[r] in arr :
                        truth = True
                        break
                else:
                        l-=1
        if truth:
                print("YES")
        else:
                print("NO")