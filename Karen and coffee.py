MAX_TEMP = 200_000

n, k, q = map(int, input().split())

diff = [0] * (MAX_TEMP + 2)  

for _ in range(n):
    l, r = map(int, input().split())
    diff[l] += 1
    diff[r + 1] -= 1

count = [0] * (MAX_TEMP + 1)
curr = 0
for i in range(1, MAX_TEMP + 1):
    curr += diff[i]
    count[i] = curr

admissible = [0] * (MAX_TEMP + 1)
for i in range(1, MAX_TEMP + 1):
    if count[i] >= k:
        admissible[i] = 1

pref = [0] * (MAX_TEMP + 1)
for i in range(1, MAX_TEMP + 1):
    pref[i] = pref[i-1] + admissible[i]

for _ in range(q):
    a, b = map(int, input().split())
    ans = pref[b] - pref[a-1]
    print(ans)
