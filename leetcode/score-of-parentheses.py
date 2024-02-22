class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        #((()()))
        #221 1 
        val = 0
        for br in s:
            if br == ")":
                val = stack[-1] + max(val*2, 1)
                stack.pop()
            else:
                stack.append(val)
                val = 0
        return val