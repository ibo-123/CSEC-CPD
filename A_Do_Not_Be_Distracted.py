for i in range(int(input())):
        n = int(input())
        s = input()
        arr = []
        for j in s:
                if j in arr and arr[-1] != j:
                        print("NO")
                        break
                elif not j in arr:
                        arr.append(j)
        else:
                print("YES")