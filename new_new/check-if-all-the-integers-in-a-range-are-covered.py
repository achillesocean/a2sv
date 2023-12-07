class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        i =  0
        ranges.sort()
        for n in range(left, right + 1):
            while i < len(ranges):
                if n >= ranges[i][0] and n <= ranges[i][1]:
                    #i += 1
                    break 
                if i == len(ranges) - 1:
                    return False
                i += 1
                
        return True
        