class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        value = 0
        window = {}
        L = 0
        for R in range(len(nums)):
            window[R] = nums[R]
            while sum(window.values()) >= target:
                if value == 0 or len(window) < value:
                    value = len(window)
                window.pop(L)
                L+=1

        return value
        

            