class Solution(object):
    def majorityElement(self, nums):
        element = None
        elementCount = 0

        for x in nums:
            if elementCount == 0:
                element = x
            if element == x:
                elementCount += 1
            else:
                elementCount -= 1

        return element


            

        