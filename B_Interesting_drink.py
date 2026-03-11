import bisect
n = int(input())
arr = list(map(int, input().split()))

arr.sort()
for i in range(int(input())):
    n = int(input())
    ans = bisect.bisect_right(arr, n)
    print(ans)
    