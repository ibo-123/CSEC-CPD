import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    f = [0] + list(map(int, input().split()))  # 1-based

    a = [0] * (n + 1)

    if n >= 3:
        # middle values
        for x in range(2, n):
            a[x] = (f[x+1] - 2*f[x] + f[x-1]) // 2

        S = sum(a[2:n])  # sum of a2..a_{n-1}
        d2 = f[2] - f[1]       # Δ(2)
        dn = f[n] - f[n-1]     # Δ(n)

        a[1] = (S - d2) // 2
        a[n] = (dn + S) // 2
    else:
        # n == 2
        # f(1) = a2,  f(2) = a1
        a[1] = f[2]
        a[2] = f[1]

    print(*a[1:])
