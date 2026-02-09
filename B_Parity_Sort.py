for i in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        arr2 = sorted(arr)
        for j in range(n):
                if arr[j]%2 != arr2[j]%2:
                        print("NO")
                        break
        else:
                print("YES")