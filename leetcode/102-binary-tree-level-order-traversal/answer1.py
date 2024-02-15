# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Own solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        arrs = {}
        def add_arr(node, level = 0):
            if level in arrs:
                arrs[level].append(node.val)
            else:
                arrs[level] = [node.val]
            if node.left:
                add_arr(node.left, level + 1)
            if node.right:
                add_arr(node.right, level + 1)
        add_arr(root)
        result = []
        i = 0
        while i < len(arrs):
            result.append(arrs[i])
            i += 1
        return result
