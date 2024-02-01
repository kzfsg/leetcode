class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        if x == 0:
            return True

        if x > 0:
            temp = x
            reversed = 0
            while temp != 0:        
                lastDigit = temp % 10
                reversed = reversed * 10 + lastDigit
                temp //= 10
            return reversed == x