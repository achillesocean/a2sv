class Solution:
    def isHappy(self, n: int) -> bool:
        visited= set()
        while n not in visited:
            if n == 1: return True
            visited.add(n)
            n = self.squares(n)

        return False

    def squares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n //= 10
        return output


        