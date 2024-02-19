class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 0
        l, r = 0, 0
        while l < len(points):
            while l < len(points) and points[l][0] <= points[r][1]:
                l += 1
            count += 1
            r = l
        return count