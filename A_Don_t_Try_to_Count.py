for  i in range(int(input())):
        n , m = map(int, input().split())
        a = input()
        b = input()
        count = 0
        if b[0] in a:
                k = a.index(b[0])
        l , r = 0 , k
        bulb = True
        while l < n and r < m:
                if a[r%n] == b[l]:
                        l+=1
                        r+=1 
                else:
                        bulb = False
                        break
        if bulb:
                print(-1)
        else:
                if m > n:
                        print(m - n)
                else:
                        print(1)