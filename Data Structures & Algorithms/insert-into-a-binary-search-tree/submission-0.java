/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode insertIntoBST(TreeNode root, int val) {
        TreeNode root1 = root;
        if (root1 == null) {
            return new TreeNode(val);
        }
        if (root1.val <= val) {
            root1.right = insertIntoBST(root1.right, val);
        }
        else if (root1.val > val) {
            root1.left = insertIntoBST(root1.left, val);
        }
    return root1;
    }
}