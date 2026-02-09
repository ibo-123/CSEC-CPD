def solve(n , s , arr):
        arr = arr + arr
        ind = 0
        ans = 0
        coun = 0
        start = False
        while ind < n*2:
                if not start and arr[ind] == s:
                        start = True
                if arr[ind] == "g" and start:
                        ans = max(ans , coun)
                        coun = 0
                        start = False
                else:
                        if start:
                                coun+=1
                ind+=1
        return max(ans , coun)
for i in range(int(input())):
        n , m = input().split()
        s = input()
        print(solve(int(n) , m , s))