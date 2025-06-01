class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def binary_search(left, right, nums, target):
            # left = 0
            # right = len(nums) - 1
    
            while left <= right:
                mid = left + (right - left) // 2  # Avoids overflow
        
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1  # Search right half
                else:
                    right = mid - 1  # Search left half
            return -1  # Target not found

        def find_rotational_index(nums):
            left = 0
            right = len(nums) - 1
    
            while left < right:
                mid = (left + right + 1) // 2
                if nums[mid] > nums[0]:
                    left = mid
                else:
                    right = mid - 1
    
            return left

        peakIndex = find_rotational_index(nums)

        if target >= nums[0]:
            return binary_search(0, peakIndex, nums, target)
        else:
            return binary_search(peakIndex + 1, len(nums) - 1, nums, target)



        


        