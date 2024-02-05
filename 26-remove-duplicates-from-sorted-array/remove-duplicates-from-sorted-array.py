class Solution(object):
    def removeDuplicates(self, nums):
        x = len(nums) - 1
        while x > 0:
            if nums[x] == nums[x-1]:
                nums.pop(x-1)
                # if x == len(nums) - 1:
                #     return
            x -= 1
        return len(nums)



# iterate through list with the first number in array
# when youre removing stuff in the array, use while loop so list index does not go out of range
# iterate backwards when removing elements, since that does not affect
        