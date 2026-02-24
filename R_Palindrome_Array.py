import sys
sys.setrecursionlimit(2000000)

def palindrom(arr , l , r):
        if l > r:
                return True
        truth = palindrom( arr , l + 1 , r - 1)
        if truth and arr[l] == arr[r]:
                return True
        else:
                return False
n = int(input())
arr = list(map(int , input().split()))
l , r = 0 , n -1
truths = palindrom(arr , l , r)
print("YES"  if truths  else "NO")