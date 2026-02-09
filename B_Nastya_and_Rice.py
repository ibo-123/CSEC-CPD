for i in range(int(input())):
        n , a ,b, c , d = map(int,input().split())
        first = (a - b , a+b )
        second = (c- d , c + d)
        if (first[1]*n >= second[0] and first[0]*n <= second[1]):
                print("Yes")
        else:
                print("No")