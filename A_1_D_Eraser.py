for i in range(int(input())):
        n ,m = map(int,input().split())
        st = input()
        idx = 0
        coun = 0
        while idx < len(st):
                if st[idx] == "B":
                        coun+=1
                        idx+=m
                else:
                        idx+=1
        print(coun)