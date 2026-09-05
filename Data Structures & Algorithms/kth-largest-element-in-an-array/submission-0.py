import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        if nums is None:
            return
        
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        
        heapq.heapify(nums)        

        i = 0

        while i != k-1:
            heapq.heappop(nums)
            i+=1

        ans = -heapq.heappop(nums)

        return ans

