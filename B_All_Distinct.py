from collections import Counter
for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        s = Counter(arr)
        nums = [s[i]-1 for i in set(s)]
        need = nums[0]
        # leng = len(arr) - nums[0]
        for i in nums[1:]:
                need = abs(need - i)
        if need > len(arr):
                print(0 if len(arr)%2==0 else 1)
                continue
        final = len((arr)) - need
        print(final)
                
                        

                      
# 1000
# 2
# 1 1
# 7
# 5 2 7 3 4 8 6
# 4
# 1 2 4 2
# 4
# 2 2 2 2
# 4
# 7 3 5 3
# 3
# 7 7 7
# 1
# 6
# 8
# 7 7 7 7 7 7 7 7
# 8
# 7 2 1 4 5 6 3 8
# 1
# 7
# 3
# 6 2 8
# 2
# 1 1
# 6
# 6 5 5 5 5 5
# 1
# 3
# 5
# 5 2 4 5 7
# 2
# 5 8
# 4
# 1 1 1 1
# 3
# 3 3 3
# 1
# 6
# 2
# 4 4
# 5
# 1 3 8 4 6
# 4
# 3 2 2 5
# 2
# 1 1
# 3
# 4 6 6
# 8
# 2 4 6 3 8 3 1 6
# 3
# 1 5 4
# 5
# 5 6 2 6 2
# 8
# 4 4 4 4 4 4 4 4
# 3
# 3 1 4
# 6
# 2 8 8 8 8 2
# 4
# 7 5 4 6
# 5
# 1 6 6 4 3
# 7
# 7 7 7 7 7 7 7
# 3
# 1 5 5
# 3
# 2 2 2
# 2
# 5 8
# 5
# 7 8 8 1 5
# 5
# 5 1 4 7 4
# 7
# 7 5 3 6 1 6 5
# 8
# 5 4 7 6 6 3 5 7









