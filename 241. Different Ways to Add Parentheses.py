class Solution:
    def diffWaysToCompute(self, express: str) -> List[int]:
        result = []
        memo = {}
        def opration(idx):
            if idx in memo:
                return memo[idx]
            result = []
            for i in range(len(idx)):
                if idx[i] in "+-*":
                    left = opration(idx[:i])
                    right = opration(idx[i+1:])
                    for r in left:
                        for l in right:
                            if idx[i] == "+":
                                result.append(r+l)
                            elif idx[i] == "-":
                                result.append(r-l)
                            else:
                                result.append(r*l)
            if not result:
                result.append(int(idx))    
            memo[idx] = result
            return result
        return opration(express)
