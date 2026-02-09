for i in range(int(input())):
        n = int(input())
        if n == 1:
                print(n)
        elif n == 2:
                ans = n**2+(n)+n**2-1
                print(ans)
        elif n == 3:
                sq = n**2
                ans = sq+sq-1+sq-2+sq-n-1
                print(ans)
        elif n == 4:
                sq = n**2
                ans = sq + 2*sq-3+(sq-n-1)
                print(ans)
        else:
                sq = n**2-1
                ans = sq+(sq-n)+(sq-n-1)+(sq-n+1)+(sq-n-n)
                print(ans)