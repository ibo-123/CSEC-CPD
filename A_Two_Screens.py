for i in range(int(input())):
        n = input()
        m = input()
        l , r = 0 , 0
        coun = 0
        truth = True
        while l < len(n) and r < len(m) and truth:
                if n[l] == m[r]:
                        coun+=1
                        l+=1
                        r+=1
                else:
                        truth = False
                        coun+=len(n[l:])+len(m[r:])
        if l < len(n) and truth:
                coun+=len(n[l:])
        elif r < len(m) and truth:
                coun+=len(m[r:])
        if n[0] == m[0]:
                coun+=1
        print(coun)
                