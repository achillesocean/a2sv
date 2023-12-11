class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        m = 1 + (n // 7)

        for i in range(1, m):
            for _ in range(7):
                money += i
                i += 1

        for _ in range(n % 7):
            money += m
            m += 1

        return money
        