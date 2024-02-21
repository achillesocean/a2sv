class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        first, pref = nums[0], 0
        for i in range(len(nums)):
            pref += nums[i]
            if i > 0 and nums[i] > first:
                first = max(ceil(pref/(i+1)), first)
        return first