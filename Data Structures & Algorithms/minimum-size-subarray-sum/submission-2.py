class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        value = 0
        window = {}
        window_sum = 0
        L = 0
        for R in range(len(nums)):
            window[R] = nums[R]
            window_sum += nums[R]
            while window_sum >= target:
                if value == 0 or len(window) < value:
                    value = len(window)
                window_sum -= nums[L]
                window.pop(L)
                L+=1

        return value
        

            