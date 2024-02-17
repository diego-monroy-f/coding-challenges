# https://leetcode.com/problems/validate-binary-search-tree/
# Own solution -- NOTE: OOPS! This does NOT solve the problem!

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
        def is_bst(node):
            is_left_correct, is_right_correct = True, True
            if node.left:
                if node.left.val >= node.val:
                    return False
                is_left_correct = is_bst(node.left)
            if node.right and is_left_correct:
                if node.right.val <= node.val:
                    return False
                is_right_correct = is_bst(node.right)
            return is_left_correct and is_right_correct
        return is_bst(root)
