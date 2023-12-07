class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # 1 2 3 4 5
        # 1 2 3 4 5 1 2 3 4 5
        return nums + nums
        