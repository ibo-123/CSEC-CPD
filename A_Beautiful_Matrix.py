coun = 0
find = 0
for i in range(5):
        arr = list(map(int , input().split()))
        if 1 in arr:
              find = arr.index(1) 
              break
        coun +=1
ans = abs(2 - coun) + abs(2 - find)
print(ans)  
                