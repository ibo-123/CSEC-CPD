for i in range(int(input())):
        n = int(input())
        m = list(map(int, input().split()))
        coun = 0
        l , r = 0 , 1
        while r < n:
            if m[l] > m[r]:
                coun += 1
                r += 2
                l += 2
            else:
                r += 1
                l += 1
        print(coun)
                
        