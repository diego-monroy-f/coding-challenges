# https://leetcode.com/problems/validate-binary-search-tree/
# Own solution -- previous one did not solve problem.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def is_bst(node, lb, rb):
            if not (lb < node.val < rb):
                return False
            is_right_correct, is_left_correct = True, True
            if node.left:
                is_left_correct = is_bst(node.left, lb, node.val)
            if node.right:
                is_right_correct = is_bst(node.right, node.val, rb)
            return is_left_correct and is_right_correct
        return is_bst(root, float("-infinity"), float("infinity"))
