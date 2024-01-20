class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count, cur = 0, 0
        vowels = ("a", "e", "i", "o", "u")
        for r in range(len(s)):
            if s[r] in vowels:
                cur += 1
            if r > k - 1 and s[r - k] in vowels:
                cur -= 1
            count = max(count, cur)
        return count
