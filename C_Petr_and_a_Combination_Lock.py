arr = [] 
for  i in range(int(input())):
        n = int(input())
        arr.append(n)
if sum(arr) == 360:
        print("YES")
else:
        arr.sort(reverse=True)
        max_ = arr[0]
        # print(arr)
        for i in arr[1:]:
                max_-=i
        if max_ == 0:
                print("YES")
        else:
                print("NO")     