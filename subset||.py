class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def subset(start , path):
            if not path[:] in res:
                res.append(path[:])
            for i in range(start , len(nums)):
                path.append(nums[i])
                subset(i+1 , path)
                path.pop()
        subset(0 , [])
        return res 
