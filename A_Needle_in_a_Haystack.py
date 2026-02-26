


import sys
from collections import Counter

input = sys.stdin.readline

for _ in range(int(input())):
    s = input().strip()
    t = input().strip()

    ct = Counter(t)
    cs = Counter(s)

    # feasibility check
    possible = True
    for ch in cs:
        if cs[ch] > ct[ch]:
            print("Impossible")
            possible = False
            break
    if not possible:
        continue

    # subtract s from t
    for ch in cs:
        ct[ch] -= cs[ch]

    first = s[0]

    left = []
    equal = []
    right = []

    for ch in sorted(ct):
        block = ch * ct[ch]
        if ch < first:
            left.append(block)
        elif ch > first:
            right.append(block)
        else:
            equal.append(block)

    equal = "".join(equal)

    if s < first * len(s):
        result = "".join(left) + s + equal + "".join(right)
    else:
        result = "".join(left) + equal + s + "".join(right)

    print(result)



















# from collections import Counter
# for i in range(int(input())):
#         ln = list(input())
#         lm = list(input())
#         m = sorted(lm)
#         n = sorted(ln)
#         l , r = 0 , 0
#         ans = ""
#         coun = {}
#         coun_n = Counter(n)
#         for k in m:
#                 if k in coun:
#                         coun[k]+=1
#                 else:
#                        coun[k] = 1
        
#         truth = True
#         if len(n) > len(m):
#                 print("Impossible")
#         else:
#                 for j in ln:
#                         if j in m:
#                            continue
#                         else:
#                                 print("Impossible")
#                                 truth = False
#                                 break
#                 while l < len(ln) and r < len(m) and truth:
#                         if ln[l] <= m[r]:
#                                 ans +=ln[l]
#                                 l +=1
#                         else:
#                                 if  not(m[r] in ln[l:]):
#                                         ans +=m[r]
#                                 r+=1
                
#                 # if l < len(ln):
#                 #         ans += ("".join(ln[l:]))
#                 # if r < len(m):
#                 #         ans += ("".join(m[r:]))
#                 # # while l < len(ln) and truth:
#                 #         ans +=ln[l]
#                 #         l +=1
#                 # while r < len(m) and truth:
#                 #         ans +=m[r]
#                 #         r+=1
#                 if truth:
#                          print(ans)