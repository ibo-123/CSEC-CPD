for i in range(int(input())):
    arr = list(map(int, input().split()))
    a,b = min(arr), max(arr)
    print(abs(a - b))