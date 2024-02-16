class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #operate on nums2
        stack = []
        map2 = {}
        for i in nums2:
            while stack and stack[-1] < i: 
                map2[stack[-1]] = i
                stack.pop()
            stack.append(i)
        for j in range(len(nums1)):
            if nums1[j] in map2:
                nums1[j] = map2[nums1[j]]
            else:
                nums1[j] = -1

        return nums1