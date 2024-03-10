class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #first, set your boundaries. then increment left to a different kind of letter, 
        #from that right boundary, check to see if you gotta expand it to include this
        #new letter.
        #each letter must appear in no more than one part=>they may need to appear in no parts
        res = []
        l1, l2, n = 0, 0, len(s)
        while l1 < n:
            l2 = l1
            temp = 1
            while l2 < l1 + temp:
                r = l2
                while r < n:
                    if s[l2] == s[r]:
                        temp = max(temp, r - l1 + 1)
                    r += 1
                l2 += 1
            res.append(temp)
            l1 += temp  

        return res
        #what are we being greedy with?only looking for the last index for each character
        #MERGE AND TRAVERSE
        