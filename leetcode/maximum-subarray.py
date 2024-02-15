class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #remove every negative prefix. 
        maxsub = nums[0]
        cursum = 0
        for num in nums:
            cursum = max(num, cursum + num)
            maxsub = max(cursum, maxsub)

        return maxsub