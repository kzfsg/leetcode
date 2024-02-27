class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashmap = {}

        for char in magazine:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        for char in ransomNote:
            if char in hashmap:
                if hashmap[char] == 0:
                    return False
                elif hashmap[char] > 0:
                    hashmap[char] -= 1
            else:
                return False
            
        return True