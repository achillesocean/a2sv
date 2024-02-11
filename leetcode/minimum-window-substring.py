class Solution:
    def minWindow(self, s: str, t: str) -> str:
        have, length, l = 0, float("inf"), 0
        test = {}
        count = {}
        res = [-1, -1]
        if t == "": return ""
        for i in t:
            test[i] = 1 + test.get(i, 0)
        need = len(test)
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            if s[r] in test and count[s[r]] == test[s[r]]:
                have += 1
            while have == need:
                if length > r - l + 1:
                    res = [l, r]
                    length = r - l + 1
                    #move my l
                count[s[l]] -= 1
                if s[l] in test and count[s[l]] < test[s[l]]:
                    have -= 1
                l += 1
        a, b = res
        return s[a:b+1] if length != float("inf") else ""