class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(cur_perm):
            nonlocal ans
            # Basecase
            if len(cur_perm) == len(nums):
                ans.append(cur_perm[:])
                return
            # 1 2 3 4
            # 2 1 3 4
            # 2 1 4 3 notice how you find permutations after every placement in the same way for every placement
            for num in nums:
                if num not in cur_perm:
                    cur_perm.append(num)
                    helper(cur_perm)
                    cur_perm.pop()
        
        helper([])
        return ans