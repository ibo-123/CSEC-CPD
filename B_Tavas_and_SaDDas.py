n = input()
leng = len(n)
ans = 0
# print(ans)
for i in range(1 ,leng ):
        ans+= 2**i
        # print(ans)
for i in range(leng):
    if n[i] == '7':
        ans += 2 ** (leng - i - 1)
                
print(ans + 1 )

