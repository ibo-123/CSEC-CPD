for i in range(int(input())):
        n , m = map(int,input().split())
        arr = input()
        r  = -10**5
        coun = 0
        for j in range(n):
                if arr[j] == "1" and j-r>=m:
                        coun+=1
                if arr[j] == "1":
                        r = j
        print(coun)     