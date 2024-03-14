class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #second variant: searching over the output space
        low = max(weights)
        high = sum(weights)
        #test for every mid
        def test(capacity):
            days_count = 1
            cur_ship = 0

            for weight in weights:
                cur_ship += weight

                if cur_ship > capacity:
                    days_count += 1
                    cur_ship = weight
                    if days_count > days: return False

            return days_count <= days

        while low <= high:
            mid = low + (high - low) // 2
            if test(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low
        