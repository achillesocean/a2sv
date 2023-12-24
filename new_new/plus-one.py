class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(num) for num in digits]
        digits = "".join(digits)
        digits = int(digits)
        digits += 1
        digits = str(digits)
        digits = [int(num) for num in digits]

        return digits        