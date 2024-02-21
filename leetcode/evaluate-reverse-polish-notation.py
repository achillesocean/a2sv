class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"*":"*", "/":"/", "+":"+", "-":"-"}
        #floor your divisions
        for token in tokens:
            if token in ops:
                first = int(stack.pop())
                second = int(stack.pop())
                if token == "/":
                    ans  = int(second / first)
                if token == "+":
                    ans = second + first
                if token == "-":
                    ans = second - first
                elif token == "*":
                    ans = second * first
                stack.append(str(ans))
                #print(stack)
            else:
                stack.append(token)
        return int(stack[-1])