class Solution:
    def sortArray(self, nums, left=None, right=None):
        if left is None: left = 0
        if right is None: right = len(nums) - 1
        if left < right:
            mid = (right+left)//2
            return self.merge(self.sortArray(nums, left, mid), self.sortArray(nums, mid + 1, right))
        else:
            return [nums[left]]

    def merge(self, l, r):
        result = []
        i = 0
        j = 0
        while i != len(l) and j != len(r):
            if l[i] > r[j]:
                result.append(r[j])
                j += 1
            else:
                result.append(l[i])
                i += 1

        while i != len(l):
            result.append(l[i])
            i += 1 
        while j != len(r):
            result.append(r[j])
            j += 1
        
        return result
