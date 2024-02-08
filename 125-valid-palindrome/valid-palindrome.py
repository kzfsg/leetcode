class Solution(object):
    def isPalindrome(self, s):
        p1 = 0
        p2 = len(s) - 1

        while p2 > p1: #doesnt matter if p2 = p1 since it is a palindrome either way
            if s[p1].isalnum() == False:
                p1 += 1
                continue
            if s[p2].isalnum() == False:
                p2 -= 1
                continue

            if s[p1].lower() != s[p2].lower():
                return False
            elif s[p1].lower() == s[p2].lower():
                p1 += 1
                p2 -= 1

        return True

        