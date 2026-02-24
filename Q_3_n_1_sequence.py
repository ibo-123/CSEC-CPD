import sys
sys.setrecursionlimit(10**6)

def sum_(coun , n):
        if n % 2 == 0:
                coun += 1
                n = n // 2
        elif n % 2 == 1 and n != 1:
                coun += 1
                n = (n * 3) + 1
        elif n == 1:
                return coun
        return sum_(coun , n)
n = int(input())
print(sum_(1 , n))
        