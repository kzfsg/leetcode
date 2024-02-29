class Solution(object):
    def isAnagram(self, s, t):
        anagram1 = {}
        anagram2 = {}

        for char in s:
            if char not in anagram1:
                anagram1[char] = 1
            else:
                anagram1[char] += 1

        for char in t:
            if char not in anagram2:
                anagram2[char] = 1
            else:
                anagram2[char] += 1

        if anagram1 == anagram2:
            return True
        else:
            return False
            


        