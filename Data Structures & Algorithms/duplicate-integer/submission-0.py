class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = []
        for digit in nums:
            if digit in check:
                return True
            else:
                check.append(digit)

        return False
        