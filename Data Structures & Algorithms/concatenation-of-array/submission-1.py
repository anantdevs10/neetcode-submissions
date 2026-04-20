class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lst = []
        for num in nums:
            lst.append(num)
        lst.extend(nums)
        return lst