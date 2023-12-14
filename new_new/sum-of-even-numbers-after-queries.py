class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                even += nums[i]
        answer = []
        prev = 0
        for q in queries:
            prev = nums[q[1]]
            nums[q[1]] += q[0]
            if prev % 2 == 0 and q[0] % 2 != 0:
                even -= prev
            if prev % 2 == 0 and q[0] % 2 == 0:
                even += q[0]
            if prev % 2 != 0 and q[0] % 2 != 0:
                even += nums[q[1]]
            #print(nums)
            print(even)
            answer.append(even)
        
        return answer
