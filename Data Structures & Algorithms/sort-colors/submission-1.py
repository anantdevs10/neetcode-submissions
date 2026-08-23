
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        count = {}
        for i in range(len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1

        left = count.get(0, 0)
        middle = count.get(1, 0)
        right = count.get(2, 0)
        print(left, middle, right)
        for i in range(left):
            nums[i] = 0
        print(nums)
        for i in range(left, left+middle):
            nums[i] = 1
        print(nums)
        for i in range(left+middle, left+middle+right):
            nums[i] = 2

        return nums
        