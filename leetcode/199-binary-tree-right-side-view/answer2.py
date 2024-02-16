# https://leetcode.com/problems/binary-tree-right-side-view/
# Own implementation -- using breath-first search (iterative)

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
        q = [root]
        while q:
            last = None
            length = len(q)
            count = 0
            while count < length:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                last = node.val
                count += 1
            result.append(last)
        return result
