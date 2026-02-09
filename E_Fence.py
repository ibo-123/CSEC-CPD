n , m = map(int,input().split())
arr = list(map(int,input().split()))
prefix = [0]*(n+1)
for i in range(n):
        prefix[i+1] = prefix[i]+arr[i]

l , r = 1 , m
min_ = prefix[r]
idx = l
while r < n+1:
        curr = prefix[r] - prefix[l-1]
        if curr < min_:
                idx = l
                min_ = curr
        r+=1
        l+=1
print(idx)
                