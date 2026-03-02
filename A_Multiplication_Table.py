import math
n , m = map(int , input().split())
coun = 0
if 1 == m:
        print(1)
        exit()
for i in range(2 ,n+1):
        if m % i == 0:
                coun+=1
        # print(i)
print(coun)