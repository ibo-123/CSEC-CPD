for i in range(int(input())):
        n = int(input())
        a = input()
        b = input()
        p = a.replace('G','B')
        q = b.replace('G','B')
        if p == q:
            print("YES")
        else:     
            print("NO")
        # print(a,b)