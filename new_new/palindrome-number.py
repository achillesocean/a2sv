class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        l, r = 0, len(x) - 1
        valid = True
        while l < r:
            if x[l] == x[r]:
                valid = True
            else:
                return False
            l, r = l + 1, r - 1
        if valid == True:
            return True
        """
        :type x: int
        :rtype: bool
        """
        