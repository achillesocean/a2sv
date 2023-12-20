class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i = 0
        s = list(s)
        while len(s) - i >= (2 * k):
            l, r = i, k + i - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            i += (2 * k)
        if (len(s) - i) >= k:
            l, r = i, k + i - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1

        if len(s) - i < k:
            l, r = i, len(s) - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1


        return "".join(s)
        