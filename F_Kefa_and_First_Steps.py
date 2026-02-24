n = int(input())
arr = list(map(int , input().split()))
coun = 0
max_ = 0
prev = arr[0]
for i in range(1 ,n):
        if arr[i] >= prev:
                coun +=1
        else:
                max_ = max(max_ , coun)
                coun = 0
        prev = arr[i]
max_ = max(max_ , coun)
print(max_ + 1)
        