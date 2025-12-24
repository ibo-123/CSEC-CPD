class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and k > 0 and  stack[-1] > i:
                stack.pop()
                k-=1
            stack.append(i)
        while k > 0:
            stack.pop()
            k-=1
        m = "".join(stack).lstrip("0") 
        return "".join(stack).lstrip("0")  if m != ""  else "0"
