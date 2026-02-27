for _ in range(int(input())):
        c = list(map(int, input().split()))
        c.sort()
        for i in range(5):
                c[0] += 1
                c.sort()
        print(c[0]* c[1]*c[2])
