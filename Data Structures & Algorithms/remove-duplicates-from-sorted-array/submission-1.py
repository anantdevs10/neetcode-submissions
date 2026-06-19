class Solution:
    def removeDuplicates(self, nums):
        p1 = 0
        p2 = 1
        write_index = 1
        if len(nums) <= 1:
            return write_index


        while p2 != len(nums):
            check = True          
            if nums[p1] != nums[p2]:
                nums[write_index] = nums[p2]
                write_index += 1
                p1+=1
                p2+=1
            elif nums[p1] == nums[p2] and check:
                print("Check happening")
                while check:
                    p2 += 1
                    if p2 == len(nums):
                        check = False
                    elif p2 != len(nums) and nums[p1] != nums[p2] :
                        print(p1, p2)
                        nums[write_index] = nums[p2]
                        write_index += 1
                        p1 = p2
                        p2 += 1
                        check = False
            print(p1, p2)
    
    
        return write_index
                






        