class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        #what if i go right to left and subtract from a number if I find a lesser number than it, else add to it
        ans = 0
        for i in range(len(s) - 1, -1, -1):
            if i + 1 < len(s) and rom_to_int[s[i]] < rom_to_int[s[i + 1]]:
                ans -= rom_to_int[s[i]]
                print(ans)
            else:
                ans += rom_to_int[s[i]]
        
        return ans