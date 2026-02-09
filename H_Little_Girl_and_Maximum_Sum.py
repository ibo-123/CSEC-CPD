n , m = map(int,input().split())
arr = list(map(int,input().split()))
prefix = [0]*(n+2)
arr.sort()

for j in range(m):
        l , r = map(int,input().split())
        prefix[l]+=1
        prefix[r+1]-=1
for i in range(1,n+1):
        prefix[i]+=prefix[i-1]
prefix = sorted(prefix[1:n+1])
ans = 0
for i in range(n):
        ans+=prefix[i]*arr[i]
print(ans)