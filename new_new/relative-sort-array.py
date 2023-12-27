class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mapping = {}
        for i, x in enumerate(arr2):
            mapping[x] = i

        arr1.sort(key=lambda x: mapping.get(x, 10000 + x))
        return arr1