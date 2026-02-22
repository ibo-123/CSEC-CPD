import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l, r = map(int, input().split())

    ans = 0

    if l <= 1 <= r:
        ans += 1

    start = max(l, 2)
    if start <= r - 1:
        ans += r - start

    print(ans)