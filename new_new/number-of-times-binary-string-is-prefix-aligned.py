class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        #keeping max index visited, and the number of ones so far.
        #a bunch of prefix sum/array algorithms
        #if index i == max_so_far
        count = 0
        curMax = -1
        for i in range(len(flips)):
            curMax = max(curMax, flips[i])
            if (i + 1) == curMax:
                count += 1

        return count
        