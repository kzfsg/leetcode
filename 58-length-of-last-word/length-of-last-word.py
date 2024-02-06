class Solution(object):
    def lengthOfLastWord(self, s):
        list = s.split()
        return len(list[len(list) - 1])
        