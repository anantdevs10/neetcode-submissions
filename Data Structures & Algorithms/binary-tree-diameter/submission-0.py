# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiameter = 0
        def find(root):
            if root == None:
                return 0
            left = find(root.left)
            right = find(root.right)
            self.maxdiameter = max(self.maxdiameter, left+right)

            return 1 + max(left, right)
        find(root)

        return self.maxdiameter
