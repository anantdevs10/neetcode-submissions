# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def check(root):
            if root == None:
                return []
        
            left = check(root.left)
            middle = [root.val]
            right = check(root.right)
        
            return left + middle + right

        values = check(root)

        for i in range(len(values)):
            if i == k-1:
                return values[i]