import sys 
sys.setrecursionlimit(200000)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x , n):
            if n == 0:
                return 1
            half = power(x , n//2)
            if n % 2 == 0:
                return half * half
            return half * half * x
            
        if n < 0 :
            x = 1 / x
        return power( x , abs(n))
        
        
        
        
        
        
        # if n<0:
        #     return pow(1/x,(abs(n)))
        # return pow(x,n)
