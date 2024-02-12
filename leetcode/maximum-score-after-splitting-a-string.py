class Solution:
    def maxScore(self, s: str) -> int:
        n= len(s)
        left = [0]*n
        right = [0]*n
        accleft = 0
        accright= 0
        for i in range(n):
            if s[i] == "0":
                accleft += 1
            if  i != n - 1:
                left[i] = accleft
            if s[n - 1 - i] == "1":
                accright += 1
            if n - 1 - i != 0:
                right[n - 1 - i] = accright
        ans = [0] * n
        for i in range(n - 1, 0, -1):
            acc = right[i] + left[i - 1]
            ans[i] = acc
        return max(ans)


        