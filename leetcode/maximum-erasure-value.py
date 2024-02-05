class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        maxsum = 0
        n = len(nums)
        l = 0
        cursum = 0
        record = [-1] * (max(nums) + 1)
        for r in range(n):
            #add to cursum after you've shrunk. then maximize
            if record[nums[r]] != -1:
                while l <= record[nums[r]]:
                    cursum -= nums[l]
                    l += 1

            record[nums[r]] = r
            cursum += nums[r]
            maxsum = max(cursum, maxsum)

        return maxsum
