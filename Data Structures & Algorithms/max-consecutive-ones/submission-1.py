class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lst = []
        count = 0
        for i in range(0,len(nums)):
            if nums[i] == 0:
                lst.append(count)
                count = 0
            elif nums[i] == 1:
                count += 1
            if i == len(nums)-1:
                lst.append(count)

        return max(lst)

        



