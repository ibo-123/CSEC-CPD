for i in range(int(input())):
        n = int(input())
        arr =list(map(int,input().split()))
        arr.sort()
        for j in range(n):
                        arr[j]= arr[j]%n if arr[j]%n!=0 else n
        l , r = 0 , n-1
        coun = 0
        while l < r:
                if arr[l]+arr[r]-1 == n:
                        coun+=2
                l+=1
                r-=1
        if coun > 0:
                print(coun)
        else:
                print(1)
        