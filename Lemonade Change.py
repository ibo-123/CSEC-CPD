class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        m = Counter()
        for i in bills:
            if i == 5:
                m[5]+=1
            elif i == 10:
                if m[5]>=1:
                    m[10]+=1
                    m[5]-=1
                else:
                    return False
            else:
                if m[5]>=1 and m[10]>=1:
                    m[5]-=1
                    m[10]-=1
                elif m[5]>=3:
                    m[5]-=3
                else:
                    return False
        return True
