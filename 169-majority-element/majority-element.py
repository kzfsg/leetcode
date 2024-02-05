class Solution(object):
    def majorityElement(self, nums):
        hashtable = {}
        for x in nums:
            if x not in hashtable:
                hashtable[x] = 1
            elif x in hashtable:
                hashtable[x] += 1
            
            if hashtable[x] > len(nums) / 2:
                return x

            

        