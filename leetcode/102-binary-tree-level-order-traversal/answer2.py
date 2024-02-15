# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Own solution using BFS/iterative solution -- after watching course

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
        result = []
        q = [root]
        level_arr = []
        per_level = len(q)
        while len(q) > 0:
            node = q.pop(0)
            level_arr.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if len(level_arr) == per_level:
                result.append(level_arr)
                level_arr = []
                per_level = len(q)
        return result
