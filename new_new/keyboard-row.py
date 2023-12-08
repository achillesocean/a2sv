class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        res = []
        r1 = "qwertyuiop"
        r2 = "asdfghjkl"
        r3 = "zxcvbnm"

        for i in range(len(words)):
            if words[i][0].lower() in r1:
                for j in range(len(words[i])):
                    if words[i][j].lower() not in r1:
                        break
                    elif j == len(words[i]) - 1:
                        res.append(words[i])
            elif words[i][0].lower() in r2:
                for j in range(len(words[i])):
                    if words[i][j].lower() not in r2:
                        break
                    elif j == len(words[i]) - 1:
                        res.append(words[i]) 
            elif words[i][0].lower() in r3:
                for j in range(len(words[i])):
                    if words[i][j].lower() not in r3:
                        break
                    elif j == len(words[i]) - 1:
                        res.append(words[i]) 
        
        return res

        