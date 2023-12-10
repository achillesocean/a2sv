class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = []
        freq = len(nums) // 3
        count = {}
        for i in range(len(nums)):
            count[nums[i]] = 1 + count.get(nums[i], 0)

        for i in nums:
            if i not in output and count[i] > freq:
                output += [i]
        return output