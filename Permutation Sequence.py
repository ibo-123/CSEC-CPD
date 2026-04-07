class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n+1))
        k-=1
        def permutation( numbers , k):
            if len(numbers) == 0:
                return ""
            fact = k // math.factorial(len(numbers) - 1)
            chose = numbers[fact]
            numbers.pop(fact)
            return str(chose) + permutation(numbers , k % math.factorial(len(numbers)))
        return permutation(numbers , k)            
        
        
        
        # one = 1
        # for i in range(1, n):
        #     one *= i
        # place = k // one + 1

