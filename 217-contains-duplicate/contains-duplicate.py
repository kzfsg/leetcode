class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}

        for number in nums:
            if number not in hashmap:
                hashmap[number] = True
            elif number in hashmap:
                return True

        return False