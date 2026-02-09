for _ in range(int(input())):
    n, m = map(int, input().split())
    d = abs(n - m)

    if d == 0:
        print(0)

    elif d != 0 and d % 2 == 0 and m > n:
        if d == 2:
            print(2)
        elif d == 1:
            print(1)
        else:
            print(2 if m % 2 == 0 else 1)

    elif d != 0 and d % 2 != 0 and m < n:
        if d == 2:
            print(2)
        elif d == 1:
            print(1)
        else:
            print(2 if n % 2 != 0 else 1)

    else:
        print(1)