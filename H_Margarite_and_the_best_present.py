for i in range(int(input())):
        n , m = map(int,input().split())
        if n == m:
                print(-n if n%2 == 1 else n)
                continue
        if n % 2 == 0:
                first = -(n) //2
        else:
                first = (n)//2 
        if m % 2 == 0:
                second = m //2
        else:
                second = (-m-1)//2
        print(second -  first)