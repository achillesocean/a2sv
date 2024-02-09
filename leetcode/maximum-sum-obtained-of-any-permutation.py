class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        freq = [0] * n
        for r in requests:
            l, r = r
            freq[l] += 1
            if r + 1 < n:
                freq[r + 1] -= 1
        acc = 0
        for i in range(len(freq)):
            acc += freq[i]
            freq[i] = acc
        posdict = defaultdict(list)#keep original posns of the frequencies
        for i in range(len(freq)):
            posdict[freq[i]].append(i)
        temp = [num for num in freq]#before sorting freq, for later summing
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        ans = [0] * n
        for i in range(n):
            j = posdict[freq[i]][-1]
            ans[j] = nums[i]
            posdict[freq[i]].pop()
        acc = 0 #the return sum
        for i in range(n):
            acc += (temp[i] * ans[i])
        return acc % ((10 ** 9) + 7)

        
        