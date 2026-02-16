import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
write = sys.stdout.write

def solve(arr, l, r, current_max):
    if l > r:
        return current_max
    
    if l == r:
        if arr[l] > current_max:
            current_max = arr[l]
        write(str(current_max) + " ")
        return current_max
    
    mid = (l + r) // 2
    
    current_max = solve(arr, l, mid, current_max)
    current_max = solve(arr, mid + 1, r, current_max)
    
    return current_max


n = int(input())
arr = list(map(int, input().split()))

solve(arr, 0, n - 1, -10**18)








# import sys
# sys.setrecursionlimit(200000)


# def maximum( arr , n , idx , max_):
#         if idx == n:
#                 return max_
#         max_ = max( max_ , arr[idx])
#         print(max_ , end=" ")
#         return maximum( arr , n , idx + 1 , max_)
# n = int(input())
# arr = list(map(int , input().split()))
# print(arr[0] , end=" ")
# maximum( arr , n , idx=1 , max_= arr[0] )