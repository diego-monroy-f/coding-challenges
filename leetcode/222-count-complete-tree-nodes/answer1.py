# https://leetcode.com/problems/count-complete-tree-nodes/
# Own solution O(log N) -- with help from course

import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        h = 1
        node = root
        while node.left:
            h += 1
            node = node.left

        result = (2**(h - 1)) - 1

        def get_val(root, i, h):
            node = root
            l = 0
            r = (2**(h - 1)) - 1
            m = (l + r) // 2
            while l != r:
                if i <= m:
                    r = m
                    node = node.left
                else:
                    l = m + 1
                    node = node.right
                m = (l + r) // 2
            return node

        def get_pos(root, l, r):
            if l == r:
                return l
            m = math.ceil((l + r) / 2)
            m_val = get_val(root, m, h)
            if m_val is not None:
                return get_pos(root, m, r)
            else:
                return get_pos(root, l, m - 1)

        pos = get_pos(root, 0, (2**(h - 1)) - 1)

        return result + pos + 1
