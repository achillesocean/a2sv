class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}   
        for i in nums:
            d[i] = 1 + d.get(i, 0)
        ans = 0
        print(d)
        for i in d:
            ans += math.comb(d[i], 2)

        return ans