class Solution(object):
    def fib(self, n):
        def fibonacci(j):
            if j == 0:
                return 0
            elif j == 1: 
                return 1
            else:
                return fibonacci(j - 1) + fibonacci(j - 2)

        return fibonacci(n)
        """
        :type n: int
        :rtype: int
        """
        