class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        #you would need to patch at most n numbers
        
        i, pref, count = 0, 0, 0
        while pref < n:
            if i < len(nums) and nums[i] <= pref + 1:
                pref += nums[i]
                i += 1
            else:
                pref += pref + 1
                count += 1

        return count
