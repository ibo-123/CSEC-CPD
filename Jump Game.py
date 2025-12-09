class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ = 0
        ind = 0
        while ind < len(nums)-1 :
            idx=nums[ind] + ind
            max_ = max(max_ , idx)
            if nums[ind] == 0 and max_ <= ind and len(nums) > 1:
                return False
            ind+=1
        if len(nums) == 1 and nums[0] == 0:
            return True
        return max_ >= len(nums)-1
