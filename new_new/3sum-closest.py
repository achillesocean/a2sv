class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = float("inf")#minimize the difference between all eligible triplets
        nums.sort()
        for n in range(len(nums)):
            l, r = n + 1, len(nums) - 1
            while l < r:
                cur = nums[n] + nums[l] + nums[r]
                if cur == target: return cur
                elif abs(closest - target) > abs(cur - target):
                    closest = cur
                if cur > target:
                    r -= 1
                elif cur < target:
                    l += 1

        return closest
                