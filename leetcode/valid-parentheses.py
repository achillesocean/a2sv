class Solution(object):
    def isValid(self, s):
        # how is a stack implemented? how is adding and popping done?
        #i should hash closing parentheses to opening ones.
        #i think the hash map is just a standard DS when doing stacks. the return value will need 
        #another DS on which it will depend. maybe that's what implements the stack.
        #i think it is standard op to use a list to implement a stack
        stack = []# note that the last value here can be accessed as [-1]
        closeToOpen = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
