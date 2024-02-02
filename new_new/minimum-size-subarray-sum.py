class Solution(object):
    def minSubArrayLen(self, target, nums):
        pref = [nums[0]] * len(nums)
        l = 0
        window = float("inf")
        for i in range(len(nums)):
            if i != 0:
                pref[i] = nums[i] + pref[i - 1]
            if pref[0] == target: return 1
            if pref[i] >= target:
                window = min(window, i + 1)
            while pref[i] - pref[l] >= target:
                window = min(window, i-l)
                l += 1

        return window if window != float("inf") else 0
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        