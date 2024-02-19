class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_count = Counter(s)
        #dddddccceee
        #ecdddddce
        #eddcccdde
        length = 0
        odd = float("-inf")
        flag = False
        for letter in letter_count:
            if letter_count[letter] % 2 != 0:
                flag = True
                length += letter_count[letter] - 1
            else:
                length += letter_count[letter]
        if flag:
            return length + 1
        else:
            return length