for i in range(int(input())):
        n , m = map(int, input().split())
        arr = list(map(int, input().split()))
        arr_ = list(map(int, input().split()))
        new = arr
        def can(mid):
                idx = 0 
                while idx < n:
                        min_ = min(new[idx] , arr_[mid] - arr[idx])
                        if idx > 0:
                                if arr[idx-1] > min_:
                                        return False
                        new[idx] = min_
                        
                        idx += 1
                return True
        left , right = 0 , m-1
        ans = False
        while left <= right:
                mid = (left + right)//2
                if can(mid):
                        ans = can(mid)
                        break
                else:
                        left = mid + 1
        print("YES" if ans else "NO")
        
        