class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counter = [0] * (1 + max(costs))
        for cost in costs:
            counter[cost] += 1
            
        ans = 0
        for i in range(1, len(counter)):
            temp = coins//i
            ans += min(temp, counter[i])
            coins -= (min(temp, counter[i]) * i)

        return ans
        