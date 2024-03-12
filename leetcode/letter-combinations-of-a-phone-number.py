class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        button = {"2":["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"],
         "7":["p","q","r","s"], "8":["t", "u", "v"], "9":["w","x","y","z"]}
        ans = []
        def backtrack(ind, cur):
            # nonlocal button
            # Each digit could only represent a single letter at a time.
            # This tells us that the length of the string will only be as long as the length of the digit string
            # Basecase
            if ind >= len(digits):
                if cur:
                    ans.append("".join(cur[:]))
                return
            #States=currently constructed string, and the step we're on==the digit we're currently decoding
            
            for char in button[digits[ind]]:
                cur.append(char)
                backtrack(ind + 1, cur)
                cur.pop()

        backtrack(0, [])
        return ans