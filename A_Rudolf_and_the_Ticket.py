for i in range(int(input())):
        n,m,k = map(int , input().split())
        arr = list(map(int , input().split()))
        arr_2 = list(map(int , input().split()))
        arr.sort()
        arr_2.sort()
        coun = 0
        for j in range(n):
                for i in range(m):
                        sun_ = arr[j] + arr_2[i]
                        if sun_ <= k:
                                coun+=1
                        else:
                                break
        print(coun)
        