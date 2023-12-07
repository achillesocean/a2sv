class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        output = [0] * len(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= maxCandies:
                output[i] = True
            else:
                output[i] = False

        return output

        