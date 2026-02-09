for i in range(int(input())):
        n = int(input())
        m = input()
        if "..." in m:
                print(2)
        else:
                print(m.count("."))