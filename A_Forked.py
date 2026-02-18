for _ in range(int(input())):
        a , b = map(int,input().split())
        Kx , Ky = map(int,input().split())
        Qx , Qy = map(int,input().split())
        move = {(a , b) , ( a , -b) , ( -a , b) , (-a , -b) , (b , a) , ( b , -a) , (-b , -a) , (-b , a)}
        
        king = set()
        for x , y in move:
                king.add((Kx + x , Ky + y))
        ans = 0
        for x , y in move:
                if  (Qx + x , Qy + y) in king:
                        ans +=1
        print(ans)
                        