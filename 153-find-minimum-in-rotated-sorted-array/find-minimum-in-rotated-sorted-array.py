class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        # If array is not rotated (already sorted)
        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2
            
            # If mid element is greater than rightmost element,
            # minimum must be in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # If mid element is less than rightmost element,
                # minimum is in the left half (including mid)
                right = mid
        
        return nums[left]