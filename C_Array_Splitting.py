n , m = map(int, input().split())
arr = list(map(int, input().split()))
if m > 1 and not m == n:
   ans = arr[m] - arr[0]
   print(ans)
elif m  == 1:
        print(arr[n-1] - arr[0])
else:
        print(0)