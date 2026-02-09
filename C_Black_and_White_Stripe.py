for i in range(int(input())):
        n ,m = map(int,input().split())
        st = input()
        l , r = 0 , m
        coun = st[:m].count("W")
        res = coun
        while r < n:
                if st[r] == "W":
                        coun+=1
                if st[l] == "W":
                        coun-=1
                res = min(res , coun)
                r+=1
                l+=1
                
        print(res)