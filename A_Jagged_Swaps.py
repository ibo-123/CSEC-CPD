for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        
        if  arr.index(min(arr)) == 0:
                print("YES")
        else:
                print("NO")