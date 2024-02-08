class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:   
        #set-up my prefix array
        pref = [0] * n
        for q in range(len(bookings)):
            l, r, k = bookings[q]
            pref[l - 1] += k
            if r < len(pref):
                pref[r] -= k

        #create solution prefix array
        acc = 0
        for r in range(len(pref)):
            acc += pref[r]
            pref[r] = acc
            
        return pref
