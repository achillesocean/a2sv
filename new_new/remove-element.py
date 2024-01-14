class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for r in nums:
            if r != val:
                k += 1
        
        while val in nums:
            nums.remove(val)
        return k
        