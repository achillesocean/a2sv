class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for i in range(len(nums)):
            count = 1
            if nums[i] - 1 not in numset:
                while nums[i] + count in numset:
                    count += 1

            longest = max(count, longest)
        return longest
        