for i in range(int(input())):
        n , a , b = map(int, input().split())
        coun = (b)*(n//2) + (n%2)*a if b/2 < a else n*a
        print(coun)