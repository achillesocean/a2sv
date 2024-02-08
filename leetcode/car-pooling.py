class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        longest = float("-inf")
        for t in trips:
            if t[2] > longest:
                longest = t[2]
    
        pref = [0] * (longest + 1)
        for t in trips:
            k, l, r = t
            pref[l] += k
            if r <= longest:
                pref[r] -= k

        acc = 0
        for i in range(len(pref)):
            acc += pref[i]
            pref[i] = acc
        temp = max(pref)
        return True if temp <= capacity else False