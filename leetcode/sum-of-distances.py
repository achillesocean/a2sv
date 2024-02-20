class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        res = [0]*len(nums)
        lookup=defaultdict(list)
        for i,x in enumerate(nums):
            lookup[x].append(i)

        for key in lookup:
            #total = [i]-[0]
            total=0
            for i in range(1, len(lookup[key])):
                total += lookup[key][i] - lookup[key][0]
            res[lookup[key][0]] = total
            for i in range(1, len(lookup[key])):
                total += (lookup[key][i] - lookup[key][i-1]) * i
                total -= (lookup[key][i] - lookup[key][i-1]) * (len(lookup[key])-(i))
                res[lookup[key][i]] = total
        
        return res