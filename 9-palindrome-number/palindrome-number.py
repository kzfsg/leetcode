import math

class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        if x == 0:
            return True

        if x > 0:
            digits = int(math.floor(math.log10(x)) + 1)
            temp = x
            reversed = 0
            for i in range(digits):        
                lastDigit = temp % 10
                reversed = reversed * 10 + lastDigit
                temp //= 10
            return reversed == x