class Solution:
    def minProcessingTime(self, pT: List[int], tasks: List[int]) -> int:
        minT = float("-inf")
        pT.sort()
        tasks.sort(reverse=True)
        
        for i in range(len(pT)):
            minT = max(minT, pT[i] + tasks[i * 4])

        return minT
        