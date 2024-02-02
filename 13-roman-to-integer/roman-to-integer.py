class Solution(object):
    def romanToInt(self, s):
        romanDictionary = {
            'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
        }
        total = 0

        for i in range(len(s)):
            if i + 1 < len(s) and romanDictionary[s[i]] < romanDictionary[s[i+1]]:
                total -= romanDictionary[s[i]]
            else:
                total += romanDictionary[s[i]]
        return total




        