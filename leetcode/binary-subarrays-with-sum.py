class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        count, cursum = 0, 0
        prefix = {0:1}
        for r in range(len(nums)):
            cursum += nums[r]
            find = cursum - k
            count += prefix.get(find, 0)
            prefix[cursum] = 1 + prefix.get(cursum, 0)
        return count