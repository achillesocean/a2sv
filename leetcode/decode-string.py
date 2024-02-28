class Solution:    
    def decodeString(self, s: str) -> str:
        nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        def helper(ind):
            word = ""
            n = ""

            while ind<len(s):
                if s[ind] == "]":
                    return [word, ind + 1]
                elif s[ind] == "[":
                    temp, ind = helper(ind + 1)
                    word += temp * int(n)
                    n = ""
                    # if n != "":
                    #     word += temp * int(n) 
                    # else:
                    #     word += temp
                elif s[ind] in nums:
                    n += s[ind]
                    ind += 1
                else:
                    word += s[ind]
                    ind += 1
            return word
        
        return helper(0)