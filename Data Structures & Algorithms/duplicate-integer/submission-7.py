class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums ==[]:
            return False
        else:
            nums.sort()
            for i in range(0, len(nums)):
                if i == len(nums)-1:
                    return False
                if nums[i] == nums[i+1]:
                    return True