def solve(a, b , m , n):
        promot = n // (m+1)
        remain  = n - promot*(m+1)
        ans = promot*min(a*m,b*(m+1))+remain*min(a,b)
        return ans
for i in range(int(input())):
        a , b = map(int,input().split())
        n, m = map(int,input().split())
        print(solve(a,b,m,n))