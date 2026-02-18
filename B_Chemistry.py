from collections import Counter

for i in range(int(input())):
        n , m = map(int , input().split())
        s = input()
        coun = Counter(s)
        need = 0
        for j in set(s):
                if coun[j] % 2 != 0:
                        need +=1
        # print(need)
        n -= m
        if n == 1:
                print("YES")
                continue
        if n % 2 == 1:
                need -=1
        if need > 0:
                need -= m
                if need > 0:
                        print("NO")
                else:
                        print("YES")
        else:
               print("YES")