class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        # Check if first k queries can make nums all zero
        def canMakeZero(k):
            diff = [0] * (n + 1)

            for i in range(k):
                l, r, val = queries[i]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val

            curr = 0
            for i in range(n):
                curr += diff[i]
                if curr < nums[i]:  # Not enough power to zero this index
                    return False
            return True

        left, right = 0, len(queries)
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if canMakeZero(mid):
                answer = mid
                right = mid - 1  # Try smaller k
            else:
                left = mid + 1

        return answer
