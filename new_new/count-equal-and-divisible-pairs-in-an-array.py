class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        pairs = 0
        for l in range(len(nums)):
            r = l + 1
            while r < len(nums):
                if nums[l] == nums[r] and (l * r) % k == 0:
                    pairs += 1
                r += 1

        return pairs
        