t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if arr[0] == 1 or arr[-1] == 1:
        print("Alice")
    else:
        print("Bob")