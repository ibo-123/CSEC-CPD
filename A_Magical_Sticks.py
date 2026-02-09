for i in range(int(input())):
        n = int(input())                
        if n%2 == 0:
            coun = n//2
        else:
            coun = n//2 + 1
        print(coun)