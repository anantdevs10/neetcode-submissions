class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(len(nums1)-1, len(nums1)-n-1,-1):
            if nums1[i] == 0:
                nums1[i] = nums2.pop(0)
        pointer1 = len(nums1)-2
        pointer2 = len(nums1)-1
        k = 0
        while k != n:
            if pointer2 == 0:
                k += 1
                pointer1 = len(nums1)-2
                pointer2 = len(nums1)-1
            if nums1[pointer1] > nums1[pointer2]:
                temp = nums1[pointer2] 
                nums1[pointer2] = nums1[pointer1]
                nums1[pointer1] = temp
            pointer1 -= 1
            pointer2 -= 1

            

            
        

        