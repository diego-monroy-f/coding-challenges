# https://leetcode.com/problems/binary-tree-right-side-view/
# Own implementation -- using depth-first search with pre-order

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        result = []
        def traverse(node, level = 0):
            if level == len(result):
                result.append(node.val)
            if node.right:
                traverse(node.right, level + 1)
            if node.left:
                traverse(node.left, level + 1)
        traverse(root)
        return result
