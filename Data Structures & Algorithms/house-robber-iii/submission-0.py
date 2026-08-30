# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def check(root):
            if root is None:
                return (0, 0)

            

            left_rob, left_not_rob = check(root.left)
            right_rob, right_not_rob = check(root.right)

            rob_val = left_not_rob + right_not_rob + root.val
            not_rob_val = max(left_rob, left_not_rob) + max(right_rob, right_not_rob)

            return (rob_val, not_rob_val)
        
        return max(check(root))
        



        