class Solution:
    def numberOfWays(self, s: str) -> int:
        #10...whenever you find a zero, add to it, the number of 1's.
        #then, whenever you find a one, you know you can create 101
        one_zero = 0
        zero_one = 0
        pref = {0:1}
        #acc = 0
        ones, zeros = 0, 0
        count = 0
        for i in range(len(s)):
            num = int(s[i])
            #acc += num
            if num == 0:
                zeros += 1
                one_zero += ones
                count += zero_one
            else:
                ones += 1
                zero_one += zeros
                count += one_zero
            #pref[acc] = 1 + pref.get(acc, 0)
        return count