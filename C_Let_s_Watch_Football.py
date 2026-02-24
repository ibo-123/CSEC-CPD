import math

a, b, c = map(int, input().split())
t = math.ceil(c * (a - b) / b)
print(t)