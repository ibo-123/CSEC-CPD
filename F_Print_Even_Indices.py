def even(arr , idx):
        if idx == -1:
                return
        if idx % 2 == 0:
                print(arr[idx] , end = " ")
        return even( arr , idx - 1)
n = int(input())
arr = list(map(int, input().split())) 
even(arr , n-1)       