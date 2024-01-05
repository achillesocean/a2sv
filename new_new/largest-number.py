class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #pad the short numbers with their first digits.
        for i in range(len(nums)):
            for j in range(0, len(nums) - 1 - i):
                temp = str(nums[j]) + str(nums[j + 1])
                temp2 = str(nums[j + 1]) + str(nums[j])
                if int(temp2) > int(temp):
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        nums = [str(num) for num in nums]
        nums = "".join(nums)
        if nums[0] == "0": return "0"
        return nums 

        mx = str(max(nums))
        mx = len(mx)
        temp = []#fill with the padded up versions
        for num in nums:
            diff = str(num)
            diff =  mx - len(diff) 
            if diff == mx:
                temp.append(str(num))
            else:
                padded = str(num)
                padded = padded + (diff * padded[-1])
                temp.append(padded)
        temp = [int(num) for num in temp]
        for i in range(len(temp)):
            for j in range(0, len(temp) - 1 - i):
                if temp[j] < temp[j + 1]:
                    temp[j], temp[j + 1] = temp[j + 1], temp[j]
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        nums = [str(num) for num in nums]
        nums = "".join(nums)
        return nums
        