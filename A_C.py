for i in range(int(input())):
        a , b , n = map(int , input().split())
        coun = 0
        while  n >= a and n >= b:
            if a > b:
                b+=a
            else:
                a+=b
            coun+=1
        print(coun)