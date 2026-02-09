for i in range(int(input())):
        m = list(map(int,input().split()))
        if len(set(m)) < 3:
                if m.count(max(m)) >= m.count(min(m)):
                        print("YES")
                        print(min(m) , max(m) , min(m))
                else:
                        print("NO")
        else:
                print("NO")