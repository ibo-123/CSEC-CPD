for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        sum_ = 0
        coun = 0
        foun = False
        for i in arr:
                if i > 0 and  foun:
                        # coun+=1
                        foun = False
                elif i < 0 and not foun:
                        foun = True
                        coun+=1
                sum_+=abs(i)
        print(sum_ , coun)