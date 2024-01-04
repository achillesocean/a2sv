class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_sum = float("-inf")
        cur_sum = 0
        l = 0
        for r in range(n):
            cur_sum += nums[r]
            if r - l + 1 == k:
                max_sum = max(max_sum, cur_sum)
                cur_sum -= nums[l]
                l += 1

        return max_sum / k
        