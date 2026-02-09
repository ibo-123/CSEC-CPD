for i in range(int(input())):
        n = int(input())
        a = input()
        coun = 1
        for j in range(1,n-1):
                if a[j-1] != a[j+1]:
                        coun+=1
        print(coun)