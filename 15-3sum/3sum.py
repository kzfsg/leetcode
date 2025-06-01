class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sortedNums = sorted(nums)
        solutionList = []

        for index, num in enumerate(sortedNums):
            twoSum = {}
            target = 0 - num
            if index > 0 and sortedNums[index] == sortedNums[index-1]:
                continue 
            for index2 in range(index + 1, len(sortedNums)):  # Only look forward!
                complement = sortedNums[index2]
                if index == index2:
                    continue
                if complement in twoSum:
                    solution = sorted([num, twoSum[complement], complement])
                    if solution not in solutionList:
                        solutionList.append(solution)                    
                twoSum[target - complement] = complement # store complement as key, value as value

        print(solutionList)
        return solutionList
        
        