class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        self.prefix_sum = [self.nums[0]] * len(self.nums)
        for i in range(1, len(self.nums)):
            self.prefix_sum[i] = self.nums[i] + self.prefix_sum[i - 1]


    def sumRange(self, left, right):
        if left == 0: return self.prefix_sum[right]
        return self.prefix_sum[right] - self.prefix_sum[left - 1]
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)