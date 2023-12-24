class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        #go over all the rows
        count = [0] * len(strs[0])
        for row in range(1, len(strs)): 
            for idx in range(len(strs[0])):
                if ord(strs[row][idx]) < ord(strs[row - 1][idx]):
                    count[idx] = 1
        counter = Counter(count)
        return counter[1]