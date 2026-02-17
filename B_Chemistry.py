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
        if n % 2 != 0:
                need -=1
        if need > 0:
                if (need - 1 > m and n % 2 ==1) or ( need > m and n % 2 == 0):
                        print("NO")
                else:
                        print("YES")
        else:
                n -= m
                if n % 2 == 1 and 4 in coun.values():
                        print("YES")
                elif n % 2 == 0:
                        print("YES")
                elif need - 1 < 0:
                        print("YES")
                else:
                        print("NO" )
                
        