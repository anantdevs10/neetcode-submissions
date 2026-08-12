
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the intersection point of the two pointers
        slow = 0
        fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
                
        # Phase 2: Find the "entrance" to the cycle (the duplicate number)
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast] # Both move 1 step now
            
        return slow

        
            
        
        