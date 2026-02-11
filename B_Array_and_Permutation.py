import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    pos = [0] * (n + 1)
    for i in range(n):
        pos[p[i]] = i
    
    possible = True
    
    for i in range(n - 1):
        if a[i] != a[i + 1]:
            if pos[a[i]] > pos[a[i + 1]]:
                possible = False
                break
    
    print("YES" if possible else "NO")
