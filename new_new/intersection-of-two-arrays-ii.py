class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = True
        if len(nums1) < len(nums2):
            temp = False

        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        res = []

        if temp:
            for key in nums1:
                res += [key] * min(nums1[key], nums2[key])
        else:
            for key in nums2:
                res += [key] * min(nums2[key], nums1[key])

        return res