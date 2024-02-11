class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        
        total = sum(nums)
        left = 0
        ans = [0] * len(nums)
        for i, n in enumerate(nums):
            right = total - n - left
            ans[i] = (i * n) - left + right - ((len(nums) - 1 - i) * n)
            left += n

        return ans