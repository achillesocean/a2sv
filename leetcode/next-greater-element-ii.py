class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ret = [0] * n

        for ind in range(n * 2):
        # We can't find a greater number for the left indices
            if not stack:
                stack.append(ind)
                continue
            while stack and nums[ind % n] > nums[stack[-1] % n]:
                ret[stack[-1] % n] = nums[ind % n]
                stack.pop()
            if ind < n:
                stack.append(ind)
        # all the indices that are left couldn't get a greater number for them
        while stack:
            ret[stack[-1] % n] = -1
            stack.pop()

        return ret