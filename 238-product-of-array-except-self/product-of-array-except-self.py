class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        answer = [1] * length

        # Compute prefix products
        prefix = 1
        for i in range(length):
            answer[i] = prefix
            prefix *= nums[i]

        # Compute suffix products and multiply
        suffix = 1
        for i in reversed(range(length)):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer