class Solution:
    def minimumSteps(self, s: str) -> int:
        s = list(s)
        l, r = 0, 0
        count =0#count of steps += r - l
        for r in range(len(s)):
            if s[r] == "0":
                while l < r and s[l] != "1":
                    l += 1
                count += r - l
                s[l], s[r] = s[r], s[l]

        return count