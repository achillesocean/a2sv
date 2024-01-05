class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #as a letter goes out of bounds, 
        test = {}
        count = {}
        res = []
        for key in p:
            test[key] = 1 + test.get(key, 0)
        l = 0
        n = len(p)
        for r in range(len(s)):
            if s[r] in test:
                count[s[r]] = 1 + count.get(s[r], 0)
            if r - l + 1 == n:
                if count == test:
                    res.append(l)
                if s[l] in test:
                    count[s[l]] -= 1
                    if count[s[l]] == 0:
                        del count[s[l]]
                l += 1
        return res

        