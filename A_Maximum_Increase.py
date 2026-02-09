n = int(input())
arr = list(map(int, input().split()))
max_ = 1
coun = 1
prev  = arr[0]
for i in arr:
        if i > prev:
                coun+=1
        else:
                max_ = max(max_, coun)
                coun = 1
        prev = i
max_ = max(max_, coun)
print(max_)
        