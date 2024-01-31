class Solution:
    def maxConsecutiveAnswers(self, ans: str, k: int) -> int:
        maxfreq, i = 0, 0
        d = {"T":0, "F":0}
        for j in range(len(ans)):
            d[ans[j]] += 1
            maxfreq = max(maxfreq, d[ans[j]])
            if j - i + 1 > maxfreq + k:
                d[ans[i]] -= 1
                i +=1 
        return len(ans) - i
       