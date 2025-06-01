class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        finalArray = []
        curr = 0
        for string in strs:
            sortedStr = str(sorted(string))
            if sortedStr not in hashmap:
                hashmap[sortedStr] = curr
                finalArray.append([string])
                curr += 1
            elif sortedStr in hashmap:
                finalArray[hashmap[sortedStr]].append(string)
        
        return finalArray
