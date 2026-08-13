class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0 
        R = len(nums) - 1


        while L <= R:
            mid = (L+R) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[L]: # ONLY the 3 left side is sorted
                if target < nums[mid] and target >= nums[L]:
                    R = mid - 1
                else: 
                    L = mid + 1
            elif nums[mid] <= nums[R]: # ONLY the 4 right side is sorted
                if target > nums[mid] and target <= nums[R]:
                    L = mid + 1
                else: 
                    R = mid - 1

            
        return -1


            

        