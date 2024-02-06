class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
#move right while you have at most two types of fruits.
#once you have more than two types, shrink from the left until you have only two.
        count, l, n = 0, 0, len(fruits)
        cur = set()
        curcount = 0
        record = [0] * (max(fruits) + 1)

        for r in range(n):
            cur.add(fruits[r])
            curcount += 1
            record[fruits[r]] += 1
            if len(cur) > 2:
                while l < r:
                    record[fruits[l]] -= 1
                    curcount -= 1
                    if record[fruits[l]] == 0:
                        cur.discard(fruits[l])
                        l += 1
                        break
                    l += 1

            count = max(curcount, count)
        return count

        