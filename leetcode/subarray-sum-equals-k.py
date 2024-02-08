class Solution(object):
    def subarraySum(self, nums, k):
        count = 0
        currSum = 0 
        prefixSums = {0 : 1}

        for i in range(len(nums)):
            currSum += nums[i]
            find = currSum - k 
            count += prefixSums.get(find, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)

        return count
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """