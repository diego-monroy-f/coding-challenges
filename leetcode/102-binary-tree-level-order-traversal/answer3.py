# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Own solution using BFS/iterative solution -- solution from course

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
        res = []
        q = [root]
        while len(q):
            level = []
            length = len(q)
            count = 0
            while count < length:
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                count += 1
            res.append(level)
        return res
