# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
          self.val = val
          self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while (curr != None):
            tmp = curr.next # stores next one from curr
            curr.next = prev # stores previous value
            prev = curr # increments prev
            curr = tmp # increments curr
        return prev
             


        
