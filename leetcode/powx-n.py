class Solution:
    def myPow(self, x: float, n: int) -> float:
        #binary exponentiation?
        def binaryExp(x, n):
            if n == 0: return 1
            if not n % 2: 
                y = binaryExp(x, n // 2)
                return (y * y)

            else:
                return x * binaryExp(x, n - 1)

        return binaryExp(x, n) if n >= 0 else 1 / binaryExp(x, abs(n))