def pyramid(n  , idx):
        if idx < 1:
                return
        space = n - idx
        star = 2*(idx) - 1
        print(space*" " + star*"*")
        return pyramid(n , idx  - 1)
n = int(input())
idx = n
pyramid(n , idx)