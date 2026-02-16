# for i in range(int(input())):
#         n = int(input())
#         arr = list(map(int,input().split()))
#         new_ = sorted(arr)
#         idx = 0
#         truth = True
#         while idx < n:
#                 if arr[idx] != new_[idx] and (idx+1)*2-1 < n:
#                         if arr[(idx+1)*2-1] != new_[idx]:
#                                 truth = False
#                                 break
#                         else:
#                                 arr[idx] , arr[(idx+1)*2-1] = arr[arr[(idx+1)*2-1]] , arr[idx]
#                 elif arr[idx] != new_[idx]:
#                         truth = False
#                         break
#                 idx+=1
#         if truth:
#                 print("YES")
#         else:
#                 print("NO")
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))  

    used = [False] * (n + 1)
    ok = True

    for i in range(1, n + 1):
        if used[i]:
            continue

        # find odd base of i
        r = i
        while r % 2 == 0:
            r //= 2

        comp = []
        x = r
        while x <= n:
            comp.append(x)
            used[x] = True
            x *= 2

        vals = sorted(a[idx] for idx in comp)
        if vals != comp:
            ok = False
            break

    print("YES" if ok else "NO")
