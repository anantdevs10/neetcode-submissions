
class Solution:
    def threeSum(self, nums):
        lst = []
        nums2 = nums[:]
        for i in range(len(nums)):
            target = -nums[i]
            seen = {}
            for j, num in enumerate(nums):
                if j != i:
                    complement = target - num
                    if complement in seen:
                        lst.append(tuple(sorted([nums[i], num, complement])))
                    seen[num] = True
        return [list(x) for x in set(lst)]