class Solution:
    def balancedString(self, s: str) -> int:
#it's gonna be a single while loop, while condition holds, minimize length
#once the test is identified.
        n = len(s) // 4
        test = {}
        counter = Counter(s)
        for chr in counter:
            if counter[chr] > n:
                test[chr] = counter[chr] - n
        if len(test) == 0: return 0
        length, l = float("inf"), 0
        k = 0
        for char in test:
            k += 1
        running = {}
        for r in range(len(s)):
            running[s[r]] = 1 + running.get(s[r], 0)
            if s[r] in test and test[s[r]] == running[s[r]]:
                k -= 1
            while k == 0 and l <= r:
                length = min(length, r - l + 1)
                running[s[l]] -= 1
                if s[l] in test and running[s[l]] < test[s[l]]:
                    k += 1
                l += 1
        return length if length != float("inf") else 0