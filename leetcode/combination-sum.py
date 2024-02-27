class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # potential states: ind, comb, cur_sum
        nums.sort()
        ans = []
        def helper(ind, comb, cursum):
            # Basecase after the bottom snippet, we wanna try a new spot to step on once we've overstepped
            # of once we've stepped the right amount of times, then try other steps.
            if ind >= len(nums): return
            if cursum >= target:
                if cursum == target:
                    ans.append(comb[:])
                return
            # for each number, a number of itself could lead to a solution.
            for i in range(ind, len(nums)):
                comb.append(nums[i])
                cursum += nums[i]
                helper(i, comb, cursum)
            # Above snippet is template of what it would look like if we kept stepping on the same 
            # spot as if anew.
            # Once we've exhausted a possible combination of steps, we wanna try new steps. other steps 
            # than the one we just took.
                comb.pop()
                cursum -= nums[i]
                # helper(i + 1, comb, cursum)

        helper(0, [], 0)
        return ans