def logs(n):
        if n == 1:
                return 0
        return 1 + logs(n//2)
n = int(input())
print(logs(n))