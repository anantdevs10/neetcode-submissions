# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next



        #reversing the second_list
        prev = None 
        curr = slow

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr           
            curr = next_node
        
        second_list = prev

        curr1 = head
        curr2 = second_list

        ans = ListNode(0)
        dummy = ans

        i = 0

        while curr1 and curr2:
            if i % 2 == 0:
                dummy.next = curr1
                curr1 = curr1.next 
            else:
                dummy.next = curr2
                curr2 = curr2.next

            dummy = dummy.next
            i += 1

        head = ans.next


         
            
        
