class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = []
        bigger = []
        equal = []
        for s in range(len(nums)):
            if nums[s] < pivot:
                smaller.append(nums[s])
        for b in range(len(nums)):
            if nums[b] > pivot:
                bigger.append(nums[b])
        for c in range(len(nums)):
            if nums[c] == pivot:
                equal.append(nums[c])
        return smaller + equal + bigger