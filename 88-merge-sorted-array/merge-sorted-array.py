class Solution(object):
    def merge(self, nums1, m, nums2, n):
        x = 0
        y = 0
        z = 0
        t = m + n
        nums1clone = nums1[:]
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
                nums1[z+1] = nums2[y]
                z += 2
                x += 1
                y += 1

        if x != m:
            while x < m:
                nums1[z] = nums1clone[x]
                z += 1
                x += 1
        elif y != n:
            while y < n:
                nums1[z] = nums2[y]
                y += 1
                z += 1
        
        return nums1
            
                    
                    
        
        # 1. compare first integer in both arrays, keep larger integer and compare with next in array with smaller integer.
        # 2. to do so, initialise another array which copies nums1
        # 3. keep going with the comparison until length m+n is achieved for nums1
        # use while loop if youre comparing two arrays side by side.