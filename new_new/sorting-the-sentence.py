class Solution:
    def sortSentence(self, s: str) -> str:
        temp = s.split()
        temp.sort(key=lambda x: x[-1])
        ans = []
        for word in temp:
            ans.append(word[:len(word) - 1])

        return " ".join(ans)
