class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] == 0 and len(nums) == 3: return 0
        #the sum of two side lengths of a triangle is always greater than the third side
        l, r = 0, 1
        maxP = float("-inf")
        while r < len(nums) - 1:
            if nums[l] + nums[r] > nums[r + 1]:
                maxP = max(maxP, nums[l] + nums[r] + nums[r + 1])
            r += 1
            l += 1

        return maxP if maxP != float("-inf") else 0
        
        