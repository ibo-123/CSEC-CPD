

for i in range(int(input())):
        n = int(input())
        m = False
        for j in range(2,int(n**(0.5))+1):
                if n % j ==0:
                        m = True
                        break
        if m:
                print("YES")
        else:
                print("NO")