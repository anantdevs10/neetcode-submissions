class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()
        for digit in nums:
            if digit in check:
                return True
            else:
                check.add(digit)

        return False
        