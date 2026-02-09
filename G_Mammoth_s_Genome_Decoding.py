n = int(input())
s = list(input())

ans = True
if n % 4 != 0:
    print("===")
    ans = False

need = n // 4


cnt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for ch in s:
    if ch in cnt:
        cnt[ch] += 1

for ch in cnt:
    if cnt[ch] > need and  ans:
        print("===")
        ans = False
        break

for i in range(n):
    if s[i] == '?':
        for ch in "ACGT":
            if cnt[ch] < need:
                s[i] = ch
                cnt[ch] += 1
                break
if all(cnt[ch] == need for ch in cnt) and ans:
    print("".join(s))
elif  ans:
    print("===")
