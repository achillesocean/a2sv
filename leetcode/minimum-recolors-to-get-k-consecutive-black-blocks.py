class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #k = desired number of consecutive black blocks
        wcount, l = 0, 0
        for r in range(k):
            if blocks[r] == "W": 
                wcount += 1
        temp = wcount
        for r in range(k, len(blocks)):
            if blocks[r] == "W":
                wcount += 1
            if blocks[l] == "W":
                wcount -= 1
                l += 1
            else:
                l += 1
            temp = min(wcount, temp)
        return temp
