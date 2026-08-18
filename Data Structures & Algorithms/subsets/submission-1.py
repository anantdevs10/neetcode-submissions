class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def dfs(i, lst):
            if i == len(nums):
                new = lst[::]
                subsets.append(new)
                return    
            lst.append(nums[i])
            dfs(i+1, lst)     
            lst.pop()
            dfs(i+1, lst)                     
            
        
        dfs(0, [])
        return subsets