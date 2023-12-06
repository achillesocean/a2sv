class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = list(s.split())
        max_len = float("-inf")
        for w in s:
            max_len = max(max_len, len(w))
        
    
        ans = []
        cur = ""
        for i in range(max_len):
            for j in range(len(s)):
                if len(s[j]) <= i:
                    cur += " "
                else:
                    cur += s[j][i]
            ans.append(cur.rstrip())
            cur = ""

        return ans
        