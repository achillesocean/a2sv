class Solution:
    def maxScore(self, points: List[int], k: int) -> int:
        maxsum = 0
        n = len(points)
        cursum = sum(points[n - k:])
        for i in range(k):
            maxsum = max(maxsum, cursum)
            cursum += points[i]
            cursum -= points[n - k + i]

        return max(maxsum, cursum)

        