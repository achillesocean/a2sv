class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                running[i] = nums[i]
            else:
                running[i] = nums[i] + running[i - 1]
        return running