class Solution(object):
    def reverseWords(self, s):
        finalString = ''
        temp = ''
        for char in s:
            if char == ' ':
                if temp:
                    finalString = ' ' + temp + finalString
                temp = ''
            else:
                temp += char
        print temp
        if temp:
            finalString = temp + finalString

        return finalString.strip()

