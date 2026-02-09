for i in range(int(input())):
        n , m = map(int, input().split())
        if n%m == 0:
                print(2)
                print(1,n-1)
        else:
                print(1)
                print(n)