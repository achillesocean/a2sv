class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        stack = {}
        for bill in bills:
            if bill == 5:
                stack[5] = 1 + stack.get(5, 0)
            elif bill == 10:
                if 5 in stack and stack[5] > 0:
                    stack[5] -= 1 
                    stack[10] = 1 + stack.get(10, 0)
                else: return False
            elif bill == 20:
                if 10 in stack and stack[10] > 0 and 5 in stack and stack[5] > 0:
                    stack[10] -= 1
                    stack[5] -= 1
                elif 5 in stack and stack[5] >= 3:
                    stack[5] -= 3
                else: return False

        return True