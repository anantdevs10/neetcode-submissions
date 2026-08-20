class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maximum = 0

        total = 0
        L = 0
        arr = []
        for R in range(len(nums)):
            if arr:
                if nums[R] <= arr[-1]:
                    arr = [nums[R]]
                    total = nums[R]
                    L = R
                else:
                    arr.append(nums[R])
                    total += nums[R]
            else:
                arr.append(nums[R])
                total += nums[R]
                
            
            if maximum < total:
                maximum = total
        
        return maximum