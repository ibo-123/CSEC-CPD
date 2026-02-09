t = int(input())
for _ in range(t):
    s, k, m = map(int, input().split())

    if k >= s:
        last_flip = (m // k) * k
        elapsed = m - last_flip
        print(max(0, s - elapsed))
    else:
        x = m % (2 * k)
        if x >= k:
            x = 2 * k - x
        print(max(0, s - x))
 