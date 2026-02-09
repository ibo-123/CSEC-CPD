import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, h = map(int, input().split())
    orig = list(map(int, input().split()))

    delta = {}  # stores increments since last crash

    for _ in range(m):
        b, c = map(int, input().split())
        b -= 1

        current = orig[b] + delta.get(b, 0)

        if current + c > h:
            delta.clear()   # crash → reset
        else:
            delta[b] = delta.get(b, 0) + c

    # build final array
    result = []
    for i in range(n):
        result.append(orig[i] + delta.get(i, 0))

    print(*result)
