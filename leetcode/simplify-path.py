class Solution:
    def simplifyPath(self, path: str) -> str:
        tmp = path.split("/")
        stack = []
        for i in tmp:
            if stack and i == "..":
                stack.pop()
            if i != "" and i != "." and i != "..":
                stack.append(i)
        return "/" + "/".join(stack)
