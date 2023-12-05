class Solution(object):
    def checkPowersOfThree(self, n):
        while n > 0:
            if n % 3 == 2:
                return False
            n = n // 3

        return True
        # distinct powers!
        # record the power that takes it above n
        max_pow = 0
        while (3 ** max_pow) <= n:
            max_pow += 1
        #print(max_pow)
        max_pow -= 1

        while n > 0:
            n -= (3 ** max_pow)
            max_pow -= 1

        return True if n == 0 else False
        """
        :type n: int
        :rtype: bool
        """
        