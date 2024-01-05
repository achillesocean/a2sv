class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0
        for point in range(len(points) - 1):
            temp = points[point + 1][0] - points[point][0]
            res = max(res, temp)

        return res

        