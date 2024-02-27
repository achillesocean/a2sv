class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # 1 2 3
        # every number will be a valid step in its own right
        # it should not look back for its next steps.
        # the absolute last element will have only itself for a subset
        def helper(ind, cur):
            # Basecase

            # What to do every step? include whatever current subset.
            ans.append(cur[:])
            
            for i in range(ind, len(nums)):
                cur.append(nums[i])
                helper(i + 1, cur)# Think, where do I wanna choose from once I've chosen 3 for example
                cur.pop()
            # return
        
        helper(0, [])
        return ans