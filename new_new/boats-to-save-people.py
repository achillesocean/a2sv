class Solution:
    def numRescueBoats(self, p: List[int], limit: int) -> int:
        #cram as much as possible into the boat
        count = 0 
        p.sort(reverse=True)
        #l = 0
        l, r = 0, len(p) - 1
        while l <= r:
            if p[r] + p[l] <= limit:
                count += 1
                l, r = l + 1, r - 1
            elif p[l] <= limit:
                count += 1
                l += 1

        return count
        