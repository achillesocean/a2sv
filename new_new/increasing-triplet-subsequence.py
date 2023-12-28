class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        f = nums[0]
        s = float("inf")
        for n in range(1, len(nums)):
            if nums[n] > s: return True
            if nums[n] > f: 
                s = nums[n]
            if nums[n] < f:
                f = nums[n]

        return False

        flag = False
        cur = nums[0]
        for n in nums:
            if flag and n > cur: return True
            if n < cur:
                flag = False
                cur = n
            elif n > cur:
                flag  = True
                cur = n

        return False 
        
        