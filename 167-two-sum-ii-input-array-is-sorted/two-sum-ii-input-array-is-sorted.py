class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        twoSum = {}
        for index, complement in enumerate(numbers):
            if complement in twoSum:
                return [twoSum[complement] + 1, index + 1]
            twoSum[target - complement] = index # store complement as key, index as value
        