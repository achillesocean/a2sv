class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0#declare the initial window pointer(s)
        charSet = set()
        res = 0
        
        for r in range(len(s)):
            #the while loop is typical when writing code that modifies the window.
            while s[r] in charSet:#note that the window is a dynamic one
                charSet.remove(s[l])
                l += 1
                
            charSet.add(s[r])#an object such as this charSet is typical.
            res = max(res, r - l + 1)#usage of the methods like max() and min(). comparing 
                                #something declared above and the window width (note the +1).
        
        return res#returning the optimized final value