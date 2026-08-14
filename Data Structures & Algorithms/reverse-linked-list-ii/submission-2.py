# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        if left == right:
            return head
        count = 1
        prev_L = None
        prev_R = None
        curr = head
        while curr:
            if count == left:
                prev_L = prev_R
                L = curr  
            elif count == right:
                R = curr  
            count += 1
            prev_R = curr # previous BEFORE R
            curr = curr.next
        # we have L and R nodes
        #iterate through L and reverse all nodes from R --> L
        after = R.next
        prev = after
        curr = L
        while curr != after:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        #connecting back out reversed Linked List
        if prev_L:
            prev_L.next = R
        else:
            head = R

        return head

        