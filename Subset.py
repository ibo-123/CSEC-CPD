class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def subset( idx , path):
            res.append(path[:])
            for i in range(idx , len(nums)):
                path.append(nums[i])
                subset( i + 1 , path)
                path.pop()
        subset( 0 , [])
        return res