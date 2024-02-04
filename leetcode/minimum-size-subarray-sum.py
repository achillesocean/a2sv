class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, minlen = 0, float("inf")
        cur = 0
        for r in range(len(nums)):
            cur += nums[r]
            while cur >= target:
                minlen = min(minlen, r - l + 1)
                cur -= nums[l]
                l += 1
            if minlen == 1: return 1
        return minlen if minlen != float("inf") else 0