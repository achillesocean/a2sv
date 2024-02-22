class Solution:
    def helper(self, right):
        if right == 0: return [1]
        prev = self.helper(right - 1)
        new = [1] * (len(prev) + 1)
        for i in range(len(new)):
            if i != 0 and i != len(new) - 1:
                new[i] = prev[i] + prev[i-1]
        
        return new
    def getRow(self, ind: int) -> List[int]:
        return self.helper(ind)#notice how I had to return it!!