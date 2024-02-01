class Solution(object):
    def twoSum(self, nums, target):
        hashtable = {}
        for index, num in enumerate(nums):
            complement = target - nums[index]
            if complement in hashtable:
                return [hashtable[complement], index]
            hashtable[num] = index

        