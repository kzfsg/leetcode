class Solution(object):
    def removeDuplicates(self, nums):
        hashtable = {}
        x = len(nums) - 1

        while x >= 0:
            if nums[x] not in hashtable:
                hashtable[nums[x]] = 1
            elif nums[x] in hashtable:
                hashtable[nums[x]] += 1
                
            if hashtable[nums[x]] > 2:
                nums.pop(x)
            x -= 1
        

