class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2) : return False
        s1c, s2c = [0] * 26, [0] * 26
        mat = 0
        for i in range(len(s1)):
            s1c[ord(s1[i]) - ord("a")] += 1
            s2c[ord(s2[i]) - ord("a")] += 1
        for i in range(26):
            mat += 1 if s1c[i] == s2c[i] else 0
        l = 0
        for r in range(len(s1), len(s2)):
            if mat == 26 : return True
            ind = ord(s2[r]) - ord("a")
            s2c[ind] += 1
            if s1c[ind] == s2c[ind]:
                mat += 1
            elif s1c[ind] + 1 == s2c[ind]:
                mat -= 1

            ind = ord(s2[l]) - ord("a")
            s2c[ind] -= 1
            if s1c[ind] == s2c[ind]:
                mat += 1
            elif s1c[ind] - 1 == s2c[ind]:
                mat -= 1
            l += 1
        return mat == 26 
            
        letters = {}
        for s in s1:
            letters[s] = 1 + letters.get(s, 0)
        temp = {}
        count = len(s1)
        for s in s2:
            if s not in temp and s in letters:
                temp[s] = 1
                count -= 1
            elif s in letters:
                if temp[s] == letters[s]:
                    temp = {}
                    count = len(s1)
                else:
                    temp[s] += 1
                    count -= 1
            else:
                count, temp = len(s1), {}
            if temp == letters: return True
        return False
        