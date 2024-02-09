class Solution(object):
    def canJump(self, nums):
        indexPotential = 0 #represents potential distance travelled from a potential "jump".
        for n in range(len(nums)):
            print(n)
            if nums[n] > indexPotential:
                indexPotential = nums[n]

            if n == len(nums) - 1 and nums[-1] == 0:
                return True
            elif indexPotential <= 0:
                return False
                
            indexPotential -= 1

        return True




# consistently changing value which starts at 0 -> initialise int variable as 0
# in order to "jump over zeroes", the index potentially travelled prior to the index before 0 has to be greater than 1
# therefore, in order to decide if the index can "jump" over the zero, the maximum possibility has to be tested
        