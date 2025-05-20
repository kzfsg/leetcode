class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        count = sum(1 for char in word if char.isupper())
        return count == len(word) or (count == 1 and word[0].isupper()) or count == 0
        