n , m = map(int,input().split())
arr = list(map(int,input().split()))
mid = n//2
arr.sort()
mid_val = arr[mid]
use = 0
ans = 0
truth = False
for i in range(mid +1, n):
        need = (arr[i]-mid_val) * (i-mid)
        if need + use > m:
                ans = mid_val+(m-use)//(i-mid)
                truth = True
                break
        use+=need
        mid_val = arr[i]
if truth:        
        print(ans)
else:
        print(mid_val+(m-use)//(n-mid))