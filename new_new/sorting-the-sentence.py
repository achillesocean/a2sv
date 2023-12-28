class Solution:
    def sortSentence(self, s: str) -> str:
        a = s.split()
        b = [0] * len(a)
        for i in a:
            b[int(i[-1]) - 1] = i[0:-1]
        return " ".join(b)
        
        temp = s.split()
        temp.sort(key=lambda x: x[-1])
        ans = []
        for word in temp:
            ans.append(word[:len(word) - 1])

        return " ".join(ans)
