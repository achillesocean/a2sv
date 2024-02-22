class Solution:
    def canJump(self, nums: List[int]) -> bool:
        good = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= good:
                good = i
        return True if good == 0 else False
        if len(nums) == 1: return True
        i = 0
        g = nums[0]
        while g > 0:
            i += 1
            g -= 1
            if i < len(nums):
                g = max(g, nums[i])
            if i >= len(nums) - 1: return True
        if i >= len(nums) - 1: return True
        return False
        n = len(nums)
        if n == 1: return True
        #[0]
        #[2, 3, 1, 3, 4] = True
        #2, 3, 0, 0, 1 = True
        #you can guarantee tht the last position is a good position
#work backwards and check if depending on the value you have there, you can possibly reach
#a good position or not; so that the position itself could be deemed accordigly.



        