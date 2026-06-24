
class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        print(nums)
        i = 0
        lst = []
        while i != len(nums)-2:
            p1 = i+1
            p2 = len(nums)-1
            target = nums[i]
            print(p1, p2, target)
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
                
            while p1 < p2:
                checksum = target + nums[p1] + nums[p2]
                if checksum > 0:
                    p2 -= 1
                elif checksum < 0:
                    p1 += 1
                else:
                    lst.append([nums[i], nums[p1], nums[p2]])
                    while p1 < p2 and nums[p1] == nums[p1 + 1]:
                        p1 += 1
                    while p1 < p2 and nums[p2] == nums[p2 - 1]:
                        p2 -= 1
                        
                    p1 += 1
                    p2 -= 1
            i+=1
        return [x for x in lst]