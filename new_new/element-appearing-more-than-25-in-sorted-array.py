class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = defaultdict(int)
        for i in arr:
            counter[i] += 1
            if counter[i] > len(arr) / 4: return i
        