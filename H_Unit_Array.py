for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        one = arr.count(1)
        minus_one = arr.count(-1)
        if n == 3:
                if minus_one == 3:
                        print(1)
                elif minus_one == 1:
                        print(1)
                else:
                        print(0)
        else:
                need = n//2 if n%2==0 else n//2 + 1
                if one >= need:
                        print(0)
                elif minus_one >= need:
                        print(minus_one - need)
                else:
                        print(0)