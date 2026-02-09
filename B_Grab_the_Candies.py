for i in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        e = 0
        o = 0
        for j in arr:
                if j % 2 == 0:
                        e += j
                else:
                        o += j
        if e > o:
                print("YES")
        else:
                print("NO")