class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        #the indices that are val are odd indices
        #frequencies are even indices
        output = []
        for i in range(0, len(nums), 2):
            output += [nums[i + 1]] * nums[i]

        return output
        