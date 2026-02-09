for i in range(int(input())):
        n , m = map(int,input().split())
        arr = list(map(int,input().split()))
        arr2 = list(map(int,input().split()))
        arr.sort()
        arr2.sort()
        
        coun = n-1
        tot = sum(arr)
        for j in arr2:
                if coun-j+1 < 0:
                        break
                tot-=arr[coun-j+1]
                coun-=j
        print(tot)