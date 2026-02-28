from collections import Counter
for i in range(int(input())):
    n = input()
    m = input()
    coun_1 = Counter(n)
    coun_2 = Counter(m)
    ans = ""
    l , r = 0 , 0 
    while l < len(n):
        if n[l] < m[r]:
            ans+=n[l]
            coun_1[n[l]]-=1
            l+=1
        elif n[l] >= m[r] and coun_2[m[r]] > coun_1[m[r]]:
            ans 
    