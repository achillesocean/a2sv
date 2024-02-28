class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #monotonically increasing stack
        stack = []
        map2 = {}
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                #map2[stack[-1]] = i - stack[-1] #temperatures[i]
                temperatures[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        while stack:
            temperatures[stack[-1]] = 0
            stack.pop()
        return temperatures