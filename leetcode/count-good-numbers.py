class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # Recursive approach. 
        # 0 1 2 3 4 5
        # 5 4 5 4 5 4
        # Construct the solution for current n depending on previous solutions.
        count = 1
        mod = (10 ** 9) + 7
        count *= (self.modExp(5, (n+1)//2, mod)) #% mod
        count *= (self.modExp(4, n//2, mod)) #% mod
        return count % mod
    
    def modExp(self, a, n, mod):
        # Implemented recursively
        if n == 0: return 1
        if n % 2 == 0: 
            y = self.modExp(a, n//2, mod)#consider modding a
            return (y*y) % mod
        else:
            return ((a % mod) * self.modExp(a, n - 1, mod)) % mod

    def modExpNaive(self, a, n, mod):
        r = 1
        a = a % mod
        while n > 0:
            if n % 2 == 1:
                r = (r * a) % mod
            a = (a * a) % mod
            n //= 2
        return r