n = int(input())
truth = False
for i in range(n // 1234567+1):
        remain = n - i * 1234567
        for j in range(remain// 123456 + 1):
                ans = remain - j * 123456
                if ans % 1234 == 0:
                        truth = True
                        break
if truth:
        print("YES")
else:
        print("NO")                
                