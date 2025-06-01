class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        pointer = 0
        maxLength = len(intervals) - 1

        while pointer < maxLength:
            if intervals[pointer][1] >= intervals[pointer + 1][0]: #combine intervals
                intervals[pointer] = [intervals[pointer][0], max(intervals[pointer][1], intervals[pointer + 1][1])]
                maxLength -= 1
                del intervals[pointer + 1]
            else:
                pointer += 1

        return intervals
            



        
        




