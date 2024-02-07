class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref = [0] * len(s)
        for shift in shifts:
            if shift[2] == 0:
                temp = -1
            else:
                temp = 1
            pref[shift[0]] += temp
            if shift[1] + 1 < len(s):
                pref[shift[1] + 1] += (-1 * temp)
        acc = 0
        for i in range(len(s)):
            acc += pref[i]
            pref[i] = acc
        inpmap = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15,
        "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}#map the input using this, then process, then map using the list
        outmap = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
        "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        output = ""
        for char in range(len(s)): 
            temp = inpmap[s[char]] + pref[char]
            output += outmap[temp % 26]
        return output

