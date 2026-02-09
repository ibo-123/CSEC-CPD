n = int(input())
arr = list(map(int,input().split()))
max_ = arr[0]
coun = 1
for i in arr:
        if i > max_:
                coun+=1
                max_ = i
print(coun)