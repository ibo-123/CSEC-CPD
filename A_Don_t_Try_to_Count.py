for  i in range(int(input())):
        n , m = map(int, input().split())
        a = input()
        b = input()
        coun = 1
        if b in a:
                coun = 0
        for j in range(5):
                a+=a
                if b in a:
                        print(coun)
                        break
                coun+=1
        else:
                print(-1)