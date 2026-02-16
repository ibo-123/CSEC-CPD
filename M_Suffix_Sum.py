def last_sum(arr , idx , m):
        if idx == len(arr):
                return 0
        if m - 1 <= idx:
               return arr[idx] +  last_sum(arr , idx + 1 , m)
n , m = map(int , input().split())
arr = list(map(int , input().split()))
print(last_sum(arr , idx=0 , m=m))x