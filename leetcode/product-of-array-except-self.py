class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #how can I use the accumulator?
        #this problem resembles a category of problems that you may identify as query returns
        #which have algo's of optimization. why query returns? think of answer[i] as an O(1) return
        #to a query which is arriving after a number of queries
        acc1, acc2, n = 1, 1, len(nums)
        pref1 = [1] * n
        pref2 = [1] * n
        for i in range(n):
            acc1 *= nums[i]
            acc2 *= nums[n - 1 - i]
            pref1[i] = acc1
            pref2[n - 1 - i] = acc2
        #[1, 2, 3, 4, 5, 6]
        #[1, 2, 6, 25, 125, 750]
        #[720, 720, 360, 120, 30, 6]
        ans = [0] * n
        for i in range(n):
            if i == 0:
                ans[i] = pref2[1]
            elif i == n - 1:
                ans[i] = pref1[n - 2]
            else:
                ans[i] = pref1[i - 1] * pref2[i + 1]
        return ans

 
        