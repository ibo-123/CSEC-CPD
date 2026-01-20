class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        idx = 0 
        num = 0
        final = []
        while num < len(nums):
            idx = num+1
            while num != idx%len(nums):
                if nums[idx%len(nums)] > nums[num]:
                    final.append(nums[idx%len(nums)])
                    break
                idx+=1
            else:
                final.append(-1)
            num+=1
        return final

