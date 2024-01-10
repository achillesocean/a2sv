class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        l, r = 0, (len(skill) - 1)
        skill.sort(reverse=True)
        chem = 0
        while l < r:
            chem += (skill[l] * skill[r])
            if l > 0:
                if abs(skill[l] - skill[l - 1]) != abs(skill[r] - skill[r + 1]):
                    return -1
            l += 1
            r -= 1

        return chem