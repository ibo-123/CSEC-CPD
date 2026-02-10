class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            idx = i
            ind = []
            direction = nums[i] > 0   # lock direction

            while len(ind) < n:
      
                if (nums[idx] > 0) != direction:
                    break

                next_idx = (idx + nums[idx]) % n

                
                if next_idx == idx:
                    break
                if next_idx == i and len(ind) >= 1:
                    return True
                if idx in ind:
                    break

                ind.append(idx)
                idx = next_idx

        return False
