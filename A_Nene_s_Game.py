for i in range(int(input())):
        n , m = map(int,input().split())
        a = list(map(int , input().split()))
        q = list(map(int , input().split()))
        for j in q:
                ans = j - a[0] + 1
                if j >= a[0]:
                    print(j - ans , end=" ")
                else:
                        print(j , end=" ")
        print()