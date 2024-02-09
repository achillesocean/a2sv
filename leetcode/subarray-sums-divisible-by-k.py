class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = {0:1}
        cursum, count = 0, 0
        quot = 1
        for r in range(len(nums)):
            cursum += nums[r]
            mod = cursum % k
            count += pref.get(mod, 0)
            pref[mod] = 1 + pref.get(mod, 0)

        return count