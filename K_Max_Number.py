def max_(arr , maxi , idx):
        if idx == len(arr) - 1:
                maxi = arr[idx]
                return maxi
        maxi = max_( arr , maxi , idx + 1)
        curr = arr[idx]
        if curr > maxi:
                maxi = curr
        return maxi
n = int(input())
arr = list(map(int , input().split()))
print(max_(arr , maxi=0 , idx=0))