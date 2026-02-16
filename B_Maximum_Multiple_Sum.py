import sys

input = sys.stdin.readline


for i in range(int(input())):
        n = int(input())
        best_x = 2
        best_k = 0
        for x in range(2 , n+1):
                k = n//x
                s = x*k*(k+1)//2 
                if s > best_k:
                        best_k = s
                        best_x = x
        print(best_x)