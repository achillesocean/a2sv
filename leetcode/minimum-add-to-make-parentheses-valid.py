class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        #counter = Counter(s)
        openPref, closePref = 0, 0
        for bracket in s:
            if bracket == "(":
                openPref += 1
            else:
                if openPref:
                    openPref -= 1
                else:
                    closePref += 1
        
        return openPref + closePref