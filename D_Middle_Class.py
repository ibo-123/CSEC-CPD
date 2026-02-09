for i in range(int(input())):
        n , m =  map(int,input().split())
        arr = list( map(int,input().split()))
        arr.sort(reverse=True)
        coun = 0
        more = 0
        need = 0
        for j in arr:
                if j >= m:
                        coun+=1
                        more+=(j-m)
                elif m <= j+more:
                        more-=(m-j)
                        coun+=1
                else:
                        break
        print(coun)
        