class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count  = {}
        l, length = 0, 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while r - l + 1 - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            length = max(length, r - l + 1)
        return length