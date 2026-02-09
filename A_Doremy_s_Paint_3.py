for i in range(int(input())):
        n = int(input())
        m = list(map(int, input().split()))
        m.sort()
        if len(m) <= 2:
                print("Yes")
        else:
                bulb = True
                l, r = 0, len(m) - 1
                sett = set()
                while l < r:
                        sum_lr = m[l] + m[r]
                        sett.add(sum_lr)
                        l += 1
                        r -= 1
                if len(sett) == 1:
                        print("Yes")
                else:
                        print("No")