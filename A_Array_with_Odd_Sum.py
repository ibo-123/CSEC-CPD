for i in range(int(input())):
        n = int(input())
        arr = list(map(int , input().split()))
        sum_ = sum(arr)
        if sum_ % 2 == 1:
                print("YES")
        else:
                eve = False
                odd = False
                for num in arr:
                        if num % 2 == 0:
                                eve = True
                        else:
                                odd = True
                if eve and odd:
                        print("YES")
                else:
                        print("NO") 