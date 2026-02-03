class Solution:
    def longestAlternatingSubarray(self, nums: List[int], m: int) -> int:
        l = -1
        maxL = 0
        for i in range(len(nums)):
            if nums[i] > m:
                l = -1
                continue
            if l == -1:
                if  nums[i] % 2 == 0:
                    maxL = max(maxL , 1)
                    l = i
                continue
        
            if nums[i]%2 == nums[i-1]%2:
                if nums[i]%2==0:
                    l = i
                    maxL = max(maxL , 1)
                else:
                    l = -1
            else:
                maxL = max(maxL , i - l + 1)
        return maxL
            
            

