class Solution:
    #def reverse(self, left, right):

    def reverseString(self, s: List[str]) -> None:
        n = len(s) - 1
        #two pointers and recursion
            #hello
            #olleh
        def reverse(left, right):
            if left > right: return
            s[left], s[right] = s[right], s[left]
            reverse(left + 1, right - 1)
        reverse(0, n)
        """
        Do not return anything, modify s in-place instead.
        """
        