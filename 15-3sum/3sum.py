class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sortedNums = sorted(nums)
        solutionList = []

        for index in range(len(sortedNums)):
            target = 0 - sortedNums[index]
            if index > 0 and sortedNums[index] == sortedNums[index-1]:
                continue 
            secondP = index + 1
            thirdP = len(nums) - 1
            
            while secondP < thirdP:
                curr = sortedNums[secondP] + sortedNums[thirdP]
                if curr > target:
                    thirdP -= 1
                elif curr < target:
                    secondP += 1
                
                else:
                    solutionList.append([sortedNums[index], sortedNums[secondP], sortedNums[thirdP]])
                    secondP += 1

                    while sortedNums[secondP] == sortedNums[secondP-1] and secondP < thirdP:
                        secondP += 1

        print(solutionList)
        return solutionList
        
        