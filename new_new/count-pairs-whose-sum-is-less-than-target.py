class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0 
        nums.sort()

        for l in range(len(nums)):
            for r in range(l + 1, len(nums)):
                if nums[l] + nums[r] < target: 
                    count += 1

        return count
        