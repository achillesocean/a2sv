class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # O(n2)
        count  =0
        nums.sort()
        n = len(nums)

        for i in range(n - 1, 1, -1):
            l, r = 0, i - 1
            while r > l:
                while nums[l] + nums[r] <= nums[i] and r > l:
                    l += 1
                count += r - l
                r -= 1
        return count