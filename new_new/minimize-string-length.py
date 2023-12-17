class Solution:
    def minimizedStringLength(self, s: str) -> int:
        res = ""
        checkHash = {}
        for i in s:
            if i not in checkHash:
                res += i
            checkHash[i] = 0

        return len(res)
        