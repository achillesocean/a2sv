class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        #calculate your distance first
        selfDist = abs(target[0]) + abs(target[1])
        for i in range(len(ghosts)):
            ghostDist = abs(ghosts[i][0] - target[0]) + abs(ghosts[i][1] - target[1])
            if ghostDist <= selfDist:
                return False

        return True
        