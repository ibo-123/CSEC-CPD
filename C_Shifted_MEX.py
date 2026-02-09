for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    need = 0
    for i in range(n-1):
            if abs(arr[i] - arr[i+1]) <= 1:
                    need = arr[i+1]
    if need == 0 and min(arr) == 0:
            need = max(arr) + 1
    elif need == 0:
            need = 0
                    
