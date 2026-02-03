class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        prefix = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            prefix[i] = prefix[i-1]+nums[i-1]
        def getsum(i,j):
            return prefix[j] - prefix[i]
        def helper(L,M):
            ans = 0
            maxL = 0
            for i in range(L+M , len(nums)+1):
                maxL = max(maxL , getsum(i-M-L , i-M))

                currentL = getsum(i-M , i)

                ans = max(ans  , maxL+currentL)
            return ans
        return max(helper(firstLen , secondLen) , helper(secondLen , firstLen))
