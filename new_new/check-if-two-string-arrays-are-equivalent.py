class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_conc = ""
        for word in word1:
            word1_conc += word
        
        word2_conc = ""
        for word in word2:
            word2_conc += word

        if word1_conc == word2_conc: return True
        else: return False