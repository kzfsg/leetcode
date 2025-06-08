class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # start with max width. reducing width but increasing height is the only way of increasing area.
        startPointer = 0
        endPointer = len(height) - 1
        maxArea = 0

        while endPointer > startPointer:
            width = endPointer - startPointer
            minHeight = min(height[startPointer], height[endPointer])
            currArea = width * minHeight

            if currArea > maxArea:
                maxArea = currArea

            if height[startPointer] > height[endPointer]:
                endPointer -= 1
            else:
                startPointer += 1

        return maxArea

        