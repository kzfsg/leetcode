class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1clone = nums1[:]
        x = 0
        y = 0
        z = 0
        
        while x < m and y < n:
            if nums1clone[x] > nums2[y]:
                nums1[z] = nums2[y]
                y += 1
                z += 1

            elif nums1clone[x] < nums2[y]:
                nums1[z] = nums1clone[x]
                x += 1
                z += 1

            elif nums1clone[x] == nums2[y]:
                nums1[z] = nums1clone[x]
                nums1[z + 1] = nums2[y]
                x += 1
                y += 1
                z += 2
        
        while x + y < m + n:
            if x < m:
                nums1[z] = nums1clone[x]
                x += 1
                z += 1
            elif y < n:
                nums1[z] = nums2[y]
                y += 1
                z += 1

        return nums1


        
        # 1. Clone nums1
        # 2. Compare nums1clone & nums2, altering nums1 and storing the numbers in order in nums1
        # 3. Repeat until length m+n for nums1 is achieved. If not, create a clause to account for the remaining numbers and append them to no.1