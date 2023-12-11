class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = ""
        for i in range(len(spaces)):
            if i > 0:
                output += s[spaces[i - 1]:spaces[i]] + " "
            else:
                output += s[:spaces[i]] + " "

        return output + s[spaces[-1]:]
        