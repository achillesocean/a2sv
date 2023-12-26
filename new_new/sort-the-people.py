class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #swap both the numbers and names at the same time
        for cur in range(1, len(names)):
            for j in range(cur, 0, -1):
                if heights[j - 1] < heights[j]:
                    heights[j], heights[j - 1] = heights[j - 1], heights[j]
                    names[j], names[j - 1] = names[j - 1], names[j]
                else:
                    break
                    
        return names

        swap = True
        while swap:
            flag = False
            for start in range(len(heights) - 1):
                if heights[start] < heights[start + 1] and not flag:
                    heights[start], heights[start + 1] = heights[start + 1], heights[start]
                    names[start], names[start + 1] = names[start + 1], names[start]
                    flag = True
                else:
                    flag = False
            if not flag:
                swap = False
        
        return names

        for m_ind in range(len(names)):
            for cur in range(m_ind + 1, len(names)):
                if heights[cur] > heights[m_ind]:
                    heights[cur], heights[m_ind] = heights[m_ind], heights[cur]
                    names[cur], names[m_ind] = names[m_ind], names[cur]

        return names

