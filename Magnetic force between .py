class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        
        position.sort()

        def canPlace(dist):
            count = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= dist:
                    count += 1
                    last = position[i]
                    if count == m:
                        return True
            return False

        left = 1
        right = position[-1] - position[0]
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            if canPlace(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer
