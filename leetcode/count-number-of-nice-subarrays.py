class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cur, l, count = 0, 0, 0
        for r in range(len(nums)):
            if nums[r] % 2 != 0:
                cur += 1
            while cur > k:
                if nums[l] % 2 != 0:
                    cur -= 1
                l += 1
            temp = l
            while cur == k:
                count += 1
                if nums[l] % 2 != 0:
                    break
                l += 1
            l = temp
        return count