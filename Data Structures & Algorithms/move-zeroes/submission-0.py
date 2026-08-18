class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        insert_pos = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1
            i+=1


