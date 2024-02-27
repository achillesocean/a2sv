class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        record = set()
        def helper(ind, sub):
            nonlocal record
            # ans.append(sub[:])
            record.add(tuple(sorted(sub[:])))
            for i in range(ind, len(nums)):
                sub.append(nums[i])
                helper(i + 1, sub)# For the current step you're on, explore further steps 
                #   from after it/that's where steps are, one after the other.
                sub.pop()
# If what's beign popped and what's being newly inserted are the same, skip the new insert

        helper(0, [])
        record=list(record)
        return record