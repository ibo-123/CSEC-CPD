for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        min_ = float('inf')    
        arr.sort() 
        prev = arr[0]
        for j in arr[1:]:
                diff = abs(j - prev)
                if diff < min_:
                        min_ = diff
                prev = j
        print(min_)