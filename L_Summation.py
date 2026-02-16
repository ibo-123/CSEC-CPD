import sys
sys.setrecursionlimit(200000)

def summation(arr , idx):
        if idx == 0:
                return arr[idx]
        return arr[idx] + summation(arr , idx - 1)
n =  int(input())
arr = list(map(int , input().split()))
print(summation(arr , n-1))