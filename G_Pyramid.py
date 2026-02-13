def pyramid(n  , idx):
        if idx == n:
                print((n-idx)*(" ")+idx*("*"))
                return idx
        print((n-pyramid(n , idx + 1))*(" ")+pyramid(n , idx + 1)*("*"))
        return pyramid(n , idx + 1)
n = int(input())
idx = 1
pyramid(n , idx)