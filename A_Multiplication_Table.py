import math
n , m = map(int , input().split())
coun = 0
for i in range(2 ,int(math.ceil(n/2))+1):
        if m % i == 0:
                coun+=2 
print(coun)