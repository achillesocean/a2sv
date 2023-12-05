class Solution(object):
    def sumOfThree(self, num):
        x = (num + 3) / 3
        if (num + 3) % 3 == 0:
            return [x - 2, x - 1, x]
        else:
            return []
        """
        :type num: int
        :rtype: List[int]
        """
        