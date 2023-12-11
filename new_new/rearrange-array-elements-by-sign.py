class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        r = 0
        for l in range(n):
            if nums[l] > 0:
                output.append(nums[l])
                while r < n:
                    if nums[r] < 0:
                        output.append(nums[r])
                        r += 1
                        break
                    r += 1
        return output
        