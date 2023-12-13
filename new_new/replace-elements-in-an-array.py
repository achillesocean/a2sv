class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        lookup = {}
        for i, x in  enumerate(nums):
            lookup[x] = i

        for x, y in operations:
            index = lookup[x]
            nums[index] = y
            lookup[y] = index
            del lookup[x]

        return nums

        #return nums