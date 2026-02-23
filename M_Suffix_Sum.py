import sys
sys.setrecursionlimit(200000)

def last_sum(n , arr , idx , m):
        if idx == n - 1:
                return arr[idx]
        if n -m  <= idx:
               return arr[idx] +  last_sum(n , arr , idx + 1 , m)
        return last_sum(n , arr , idx + 1 , m)
n , m = map(int , input().split())
arr = list(map(int , input().split()))
idx = 0
print(last_sum(n , arr , idx , m))