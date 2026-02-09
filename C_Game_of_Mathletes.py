for i in range(int(input())):
        n , m = map(int,input().split())
        arr = list(map(int,input().split()))
        coun = 0 
        arr.sort()
        l , r = 0 , n-1
        while l < r:
                if arr[l] + arr[r] == m:
                        coun+=1
                        l+=1
                        r-=1
                elif arr[l]+arr[r] > m:
                        r-=1
                else:
                        l+=1
        print(coun)