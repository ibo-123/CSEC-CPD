class Solution:
    def monkeyMove(self, n: int) -> int:
        def power(n):
            if n == 1:
                return 2
            half = power(n // 2)
            if n % 2 == 0:
                return (half * half) %(10**9 + 7) 
            return (half*half * 2)%(10**9 + 7)

        return (power(n) - 2)%(10**9 + 7)
        # return (2**n - 2)%(10**9 + 7)
