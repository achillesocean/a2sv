class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        series_sum = ((n ** 2) / 2) + (n / 2)
        return int(series_sum - sum(nums))
        