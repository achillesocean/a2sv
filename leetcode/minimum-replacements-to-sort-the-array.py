import math
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        d = nums[n - 1]
        for i in range(n - 2, -1, -1):
            temp = nums[i]
            if temp > d:
                spaces = math.ceil(temp/d)
                count += spaces - 1
                d = temp // spaces
            else:
                d = nums[i]

        return count
