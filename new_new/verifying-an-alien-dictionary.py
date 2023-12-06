class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        if len(words) == 1: return True
        for i in range(1, len(words)):
            if order.index(words[i][0]) < order.index(words[i - 1][0]):
                return False
        
        for i in range(1, len(words)):
            if words[i][0] == words[i - 1][0]:
                j = 1
                while j < len(words[i]) and j < len(words[i - 1]):
                    if order.index(words[i][j]) < order.index(words[i - 1][j]):
                        print(words[i][j], words[i - 1][j])
                        return False
                    j += 1
                if words[i] in words[i - 1] and len(words[i]) < len(words[i - 1]):
                    return False

        return True
                