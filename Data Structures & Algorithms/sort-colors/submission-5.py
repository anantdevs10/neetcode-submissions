
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L = 0
        M = 0
        R = len(nums)-1


        while M <= R:
            if nums[M] == 0:
                nums[L], nums[M] = nums[M], nums[L]
                L+=1
                M+=1
            elif nums[M] == 1:
                M+=1
            elif nums[M] == 2:
                nums[M], nums[R] = nums[R], nums[M]
                R-=1

            

