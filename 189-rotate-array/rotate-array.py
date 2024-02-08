class Solution(object):
    def rotate(self, nums, k):
        rotatedList = []
        k %= len(nums)
        x = len(nums) - 1
        n = len(nums)
        while x >= n - k:
            rotatedList.append(nums.pop(x))
            x -= 1
        
        nums[:0] = reversed(rotatedList)
        return nums

        