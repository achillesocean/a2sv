class Solution:
    def breakPalindrome(self, p: str) -> str:
        if p == "a"*len(p): return "a"*(len(p)-1) + "b" if len(p) > 1 else ""
        if len(p) % 2 != 0:
            floor = len(p) // 2
            for c in range(len(p)):
                if p[c] != "a" and c != floor:
                    return p[:c] + "a" + p[c+1:] if c+1 < len(p) else p[:c] + "a"
                if p[c] == "a" and c == len(p) - 1:
                    return p[:c] + "b"
        else:
            for c in range(len(p)):
                if p[c] != "a":
                    return p[:c] + "a" + p[c+1:] if c+1 < len(p) else p[:c] + "a"
                if c == len(p) - 1 and p[c] == "a":
                    return p[:c] + "b"
                
        return ""