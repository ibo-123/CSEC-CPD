from collections import Counter
for _ in range(int(input())):
        n,m = map(int , input().split())
        p = input()
        s = Counter(p)
        alpha = "ABCDEFG"
        need = 0
        for i in alpha:
                if s[i] < m:
                        need += (m - s[i])
        print(need)
        