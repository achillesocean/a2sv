class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        #for each prefix span, create the suffix, that's why you multiply
        #3, 1, 2, 4
        #_  
        #   _______
        #      ____
        #         _
        #span=number of elements when our windows is extended to them still have the previous minimum
        stack = [] #append when the left stack
        ret = [0] * len(arr)
        for i in range(len(arr)):
            temp = (i, arr[i])
            while stack and stack[-1][1] > temp[1]:
                stack.pop()
            if len(stack) == 0:
                ret[i] = temp[0] + 1
            else:
                ret[i] = temp[0] - stack[-1][0]
            stack.append(temp)

        stack = []
        for i in range(len(arr) - 1, -1, -1):
            temp = (i, arr[i])
            while stack and stack[-1][1] >= temp[1]:
                stack.pop()
            if len(stack) == 0:
                ret[i] *= (len(arr) - temp[0])
            else:
                ret[i] *= (stack[-1][0] - temp[0])
            stack.append(temp)
        ans = 0
        for num in range(len(ret)):
            ans += (arr[num] * ret[num])
        return ans % ((10 ** 9) + 7)