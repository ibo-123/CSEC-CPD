for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    pos = [0] * (n + 1)
    for i in range(n):
        pos[arr[i]] = i

    L = R = pos[1]
    ok = True

    for x in range(2, n + 1):
        if pos[x] == L - 1:
            L -= 1
        elif pos[x] == R + 1:
            R += 1
        else:
            ok = False
            break

    print("YES" if ok else "NO")
