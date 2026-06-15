class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for i in range(len(nums)):
            counter[nums[i]] = 1 + counter.get(nums[i], 0)

        max_ = 0
        max__ = -1
        for key, value in counter.items():
            if value >= max_:
                max_ = value
                max__ = key
        return max__

        