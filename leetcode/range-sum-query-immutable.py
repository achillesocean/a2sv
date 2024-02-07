class NumArray:

    def __init__(self, nums: List[int]):
        self.pref = [nums[0]] * len(nums)
        for r in range(1, len(nums)):
            self.pref[r] = self.pref[r - 1] + nums[r]
    def sumRange(self, left: int, right: int) -> int:
        return self.pref[right] - self.pref[left - 1] if left > 0 else self.pref[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)