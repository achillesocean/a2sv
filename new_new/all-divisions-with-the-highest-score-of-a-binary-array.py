class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        output = [0] * (len(nums) + 1)
        zeros = 0
        for i in nums:
            if i == 0:
                zeros += 1
        ones = len(nums) - zeros
        highest = ones
        output[0] = ones
        res = [0]
        for i in range(1, len(output)):
            if nums[i - 1] == 0:
                output[i] = output[i - 1] + 1
            else:
                output[i] = output[i - 1] - 1
            #highest = max(output[i], highest)
            if output[i] > output[res[0]]:
                res.clear()
                res.append(i)
            elif output[i] == output[res[0]]:
                res.append(i)        
        
        return res

        