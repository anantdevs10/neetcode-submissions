# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        strategy:

        traverse left and right
        keep record of good nodes as you traverse
        have a counter while traversing and updates the maximum number of the good node

        '''
        
        def search(root, maximum):
            if root == None:
                return 0

            if root.val >= maximum:
                return 1 + search(root.left, root.val) + search(root.right, root.val)
            else:
                return search(root.left, maximum) + search(root.right, maximum)
            


        return search(root, root.val)