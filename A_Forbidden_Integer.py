for i in range(int(input())):
        n , k , x = map(int , input().split())
        if x != 1:
                print("YES")
                print(n)
                for j in range(n):
                                print(1 , end=" ")
                print()
        else:
                if k < 3 and (n % 2 == 1 or  k != 2):
                        print("NO")
                else:
                        print("YES")
                        print(n//2)
                        for j in range(n//2-1):
                                print(2 , end=" ")
                        if n % 2 == 0:
                                print(2)
                        else:
                                print(3)
                        # print()
        