from collections import Counter
n = []
for i in range(int(input())):
        m = input()
        n.append(m)
s = Counter(n)
for i in n:
        if s[i] > 0:
                print("OK")
                if s[i]:
                        print(i+f"{s[i]-1}")
                        s[i]=0
                        
        