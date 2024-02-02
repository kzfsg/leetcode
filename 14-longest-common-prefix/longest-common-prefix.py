class Solution(object):
    def longestCommonPrefix(self, strs):

        commonPrefix = strs[0]
        shortestLength = min(len(s) for s in strs)
        commonPrefix = commonPrefix[:shortestLength]

        for i in range(shortestLength):
            for x in range(len(strs) - 1):
                if strs[0][i] != strs[x+1][i]:   # does not remove since shortest length prevents it from reaching b
                    commonPrefix = commonPrefix[:i]
        return commonPrefix


                    

# 1. initialise variable to store commonprefix
# 1(a). find shortest length of all strings in str.
# 1(b). allow common prefix to take highest possible prefix using shortest length to slice it
# 2. iterate through remaining strings to find if individual characters in common prefix is present. if absent, slice the remaining string in commonPrefix