for j in range(int(input())):
        n = int(input())
        m = list(map(int, input().split()))
        min_ = -10**10
        coun = 0
        for i in m:
               if min_+1 < i:
                   coun += 1
                   min_ = i
        print(coun) 
        