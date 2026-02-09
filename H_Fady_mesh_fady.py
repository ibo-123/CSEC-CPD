import math
n = int(input())
m = list(map(int,input().split()))
y = math.lcm(*m)
coun = 0
for i in m:
        coun+=(y//i)
print(coun)