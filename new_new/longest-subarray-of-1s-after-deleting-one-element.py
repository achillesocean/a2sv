class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #count of 0's in subarray must be at most 1 at any given moment
        l, count, cur, longest = 0, 0, 0, 0
        flag = False
        for r in range(len(nums)):
            if nums[r] == 1:
                cur += 1
            else:
                flag = True
                count += 1
                if count > 1:
                    while nums[l] != 0:
                        cur -= 1
                        l += 1
                    l += 1
                    count -= 1
            longest = max(cur, longest)
        return longest if flag else longest - 1        