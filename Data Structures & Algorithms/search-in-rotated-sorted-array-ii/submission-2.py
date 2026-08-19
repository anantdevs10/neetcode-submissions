class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L+R) // 2

            if nums[mid] == target:
                return True

            elif nums[mid] > nums[L]:
                if target < nums[mid] and target >= nums[L]:
                    R = mid
                else:
                    L = mid + 1

            elif nums[mid] < nums[R]:
                if target > nums[mid] and target <= nums[R]:
                    L = mid+1
                else:
                    R = mid
            elif nums[mid] == nums[L]:
                L += 1
            elif nums[mid] == nums[R]:
                R -= 1
        return False
