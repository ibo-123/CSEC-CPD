for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        one = arr.count(1)
        minus = arr.count(-1)
        if one >= minus:
                if minus%2==0:
                        print(0)
                else:
                        print(1)
        elif one < minus:
                mid = n//2 if n%2 ==0 else n//2+1
                dif =  mid - one
                if n <= 3:
                        print(n-one)  
                        continue 
                print(dif)
                