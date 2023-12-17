class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        print(s)
        s = [s[i] for i in range(len(s) - 1, -1, -1)]
        s = " ".join(s)
        return s
        