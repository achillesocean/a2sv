class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        counter = Counter(nums)
        dist = [nums[0]]

        for n in range(1, len(nums)):
            if nums[n] != dist[-1]:
                dist.append(nums[n])

        ops = [0] * len(dist)
        for i in range(len(ops)):
            if i + 1 < len(ops):
                ops[i] = counter[dist[i]]
                if i > 0:
                    ops[i] += ops[i - 1]
        print(dist)
        return sum(ops)
