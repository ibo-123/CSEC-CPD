save = {}
def fibon(n):
        if n < 2:
                save[n] = n
                return save[n]
        if n in save:
                return save[n]
        save[n] = fibon(n - 1) + fibon( n - 2)
        return save[n] 
print(fibon(5))