class Solution(object):
    def strStr(self, haystack, needle):
        count = 0
        x = 0
        y = 0
        while x < len(needle) and y < len(haystack):
            if needle[x] == haystack[y]:
                count += 1
                x += 1
                y += 1
            else:
                x = 0
                y -= (count - 1)
                count = 0

            if count == len(needle):
                return y - len(needle)
       
        return -1
        