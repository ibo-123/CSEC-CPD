for  i in range(int(input())):
        n = int(input())
        if n%2 == 0 and n > 3:
            print(0)
        elif n == 2:
            print(2)
        elif n == 3:
            print(3)
        else:
                print(1)