# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        curr = head
        counter = 0

        while curr != None:
            counter += 1
            curr = curr.next

        remove = counter - n
        check = 1

        removed = False

        if remove == 0:
            return head.next

        prev = head
        curr = head.next

        while curr != None:
            if check == remove:
                prev.next = curr.next
                curr.next = None
                return head
            check += 1
            curr = curr.next
            prev = prev.next

        return head

            
        