
import math
for i in range(int(input())):
    a , b = map(int,input().split())
    if b%a == 0:
        print(b*(b//a))
    else:
        print(b*((a//math.gcd(a,b))))