# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def check(node, depth):
            if node == None:
                return []
            
            if depth == len(res):
                res.append(node.val)

            right = check(node.right, depth+1)
            left = check(node.left, depth+1)
        
        check(root, 0)
        return res