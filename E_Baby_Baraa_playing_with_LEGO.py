n , m = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(m):
        l , r = map(int,input().split())
        if l > 1:
                print(arr[0])
        elif r < n:
                print(arr[-1])