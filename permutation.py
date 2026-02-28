class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permute(path , used , nums):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                path.append(nums[i])
                permute(path , used , nums)

                path.pop()
                used[i] = False
        permute( [] , [False]*(len(nums)) , nums)
        return res