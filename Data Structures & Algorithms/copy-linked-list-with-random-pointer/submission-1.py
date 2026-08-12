"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ans = Node(0, None)
        dummy = ans

        curr = head
        hashmap = {}
        hashmap2 = {}
        i = 0
        while curr:
            hashmap[curr] = i
            hashmap2[i] = Node(curr.val)
            curr = curr.next
            i += 1

        curr = head
        i = 0
        while curr:
            if curr.random:
                indx = hashmap[curr.random]
                hashmap2[i].random = hashmap2[indx]
            else:
                hashmap2[i].random = None
            curr = curr.next
            i+=1
        for j in range(i):
            dummy.next = hashmap2[j]
            dummy = dummy.next
        return ans.next
        


