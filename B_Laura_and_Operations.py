for j in range(int(input())):
        a , b , c = map(int, input().split())
        can1 = 1 if b % 2 == c % 2 else 0
        can2 = 1 if a % 2 == c % 2 else 0
        can3 = 1 if a % 2 == b % 2 else 0
        print(can1 , can2 , can3)