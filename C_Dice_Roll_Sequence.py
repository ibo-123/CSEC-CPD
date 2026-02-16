import sys
input = sys.stdin.readline

INF = 10**18

# adjacency: v can follow u if u != v and u + v != 7
adj = [[False]*7 for _ in range(7)]
for u in range(1, 7):
    for v in range(1, 7):
        if u != v and u + v != 7:
            adj[u][v] = True

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0]*7  # 1..6, start free for first position

    for x in a:
        new_dp = [INF]*7
        for v in range(1, 7):
            cost = 0 if v == x else 1
            best = INF
            for u in range(1, 7):
                if adj[u][v]:
                    if dp[u] < best:
                        best = dp[u]
            new_dp[v] = best + cost
        dp = new_dp

    print(min(dp[1:7]))
