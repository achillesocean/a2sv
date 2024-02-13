class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        dist = set()
        distCount = 0
        for i in nums:
            if i not in dist:
                distCount += 1
                dist.add(i)

        count, record, l = 0, {}, 0
        ret = 0
        for r in range(len(nums)):
            c = nums[r]
            record[c] = 1 + record.get(c, 0)
            if record[c] == 1:
                count += 1
            while count == distCount:
                ret += len(nums) - r
                x = nums[l]
                record[x] -= 1
                if record[x] == 0:
                    count -= 1
                    del record[x]
                l += 1
        return ret

