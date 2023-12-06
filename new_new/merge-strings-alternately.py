class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        j = 0
        merged = ""
        while j < len(word1) and j < len(word2):
            merged += word1[j] + word2[j]
            j += 1

        if j < len(word1):
            merged += word1[j:]
        elif j < len(word2):
            merged += word2[j:]

        return merged