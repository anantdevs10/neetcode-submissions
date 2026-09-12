class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0] * len(nums1)

        p1 = 0
        p2 = 0
        while p1 < len(nums1):
            p2 = nums2.index(nums1[p1])
            while p2 < len(nums2) and nums2[p2] <= nums1[p1]:
                p2 += 1 
            if p2 == len(nums2):
                ans[p1] = -1
            else:
                ans[p1] = nums2[p2]
            p1 += 1
        return ans

            
        