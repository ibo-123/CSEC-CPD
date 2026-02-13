def binary(n):
        if n == 1 :
                return "1"
        if n % 2 == 0:
                return "0" + binary(n//2)
        return "1" + binary(n//2)
for i in range(int(input())):
        n = int(input()) 
        print(binary(n)[::-1])            