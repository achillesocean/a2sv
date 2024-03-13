class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #two searches?
        res = [-1, -1]
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1

        res[0] = int(l) if l < len(nums) and nums[l] == target else -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1

        res[1] = int(r) if r >= 0 and nums[r] == target else -1

        return res

        #4 4 4 4 5 6 7 8 9