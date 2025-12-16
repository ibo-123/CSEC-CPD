class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_ = {} 
        for i in nums2:
            while stack and stack[-1] < i:
                next_[stack[-1]] = i
                stack.pop() 
            stack.append(i)
            next_[i] = -1
        final = []
        for i in nums1:
            final.append(next_[i])
        return final            
            
