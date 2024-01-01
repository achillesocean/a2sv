class Solution:
    def sortColors(self, nums: List[int]) -> None:
        storage = [0] * (max(nums) + 1)
        for i in range(len(nums)):
            storage[nums[i]] += 1

        #override nums
        ind = 0
        for i in range(len(storage)):
            for _ in range(storage[i]):
                nums[ind] = i
                ind += 1
        
        """
        Do not return anything, modify nums in-place instead.
        """
        