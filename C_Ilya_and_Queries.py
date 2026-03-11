n = input()
m = int(input())
preifx = [0] * (len(n) + 1)
for i in range(1, len(n)):
        if n[i - 1] == n[i]:
                preifx[i] = preifx[i - 1] + 1
        else:
                preifx[i] += preifx[i - 1]
for i in range(m):
    l, r = map(int, input().split())
    print(preifx[r - 1] - preifx[l - 1])
#     print(preifx)