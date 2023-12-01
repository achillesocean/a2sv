class Solution(object):
    def longestCommonPrefix(self, strs):
        #longest common is the minumum of common between consecutive words
        old = strs[0]
        length = len(old)
        if len(strs) == 1:
            return old
        cur = 0 
        for w in range(1, len(strs)):
            for i in range(min(len(old), len(strs[w]))):
                if strs[w][i] == old[i]:
                    cur += 1
                else: 
                    break
            length = min(cur, length)
            old = strs[w]
            cur = 0
        print(length)
        return strs[0][:length]
        """
        :type strs: List[str]
        :rtype: str
        """
        