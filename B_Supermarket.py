b,c = map(int,input().split())
min_ = [None,None]
for i in range(b):
        m , n = map(int,input().split())
        if min_[0] == None:
                min_[0],min_[1] = m , n
        else:
                if min_[1]/min[0] > n/m:
                         min_[0],min_[1] = m , n

                        
        