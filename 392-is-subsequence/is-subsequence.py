class Solution(object):
    def isSubsequence(self, s, t):
        count1 = 0
        count2 = 0
        while count1 < len(s) and count2 < len(t):
            if s[count1] == t[count2]:
                count1 += 1
                count2 += 1
            elif s[count1] != t[count2]:
                count2 += 1

        if count2 == len(t) and count1 == len(s):
                return True
        elif count2 == len(t) and count1 != len(s):
                return False

        return True

            
            
        