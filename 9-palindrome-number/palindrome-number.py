class Solution(object):
    def isPalindrome(self, x):
        xstring = str(x)
        xlisted = list(xstring)
        reversed_xlisted = xlisted[::-1]
        return xlisted == reversed_xlisted
        