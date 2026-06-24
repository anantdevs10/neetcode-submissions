class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        lst = []
        i = 0
        while i != (len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                i+=1
                continue
            j = i + 1
            while j != len(nums)-2:
                if j > i+ 1 and  nums[j] == nums[j-1]:
                    j += 1
                    continue
                p1 = j + 1
                p2 = len(nums)-1
                while p1 < p2:
                    checksum = nums[i] + nums[j] + nums[p1] + nums[p2]
                    if checksum < target:
                        p1 += 1
                    elif checksum > target:
                        p2 -= 1
                    else:
                        print("Added!")
                        lst.append([nums[i], nums[j], nums[p1], nums[p2]])
                        while p1 < p2 and nums[p1] == nums[p1 + 1]:
                            p1 += 1
                        while p1 < p2 and nums[p2] == nums[p2 - 1]:
                            p2 -= 1
                        p1 += 1
                        p2 -= 1
                j += 1
            i += 1

        return lst
    
sol = Solution()
sol.fourSum([1,-1,1,-1,1,-1], 2)

