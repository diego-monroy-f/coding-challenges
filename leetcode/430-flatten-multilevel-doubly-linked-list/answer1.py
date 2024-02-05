# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
# First solution -- own

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def traverse(node):
            current = node
            start = node
            end = node
            while current:
                end = current
                if not current.child:
                    current = current.next
                else:
                    _next = current.next
                    h, t = traverse(current.child)
                    end = t
                    current.child = None
                    current.next = h
                    h.prev = current
                    t.next = _next
                    if _next:
                        _next.prev = t
                    current = _next
            return start, end
        _h, _ = traverse(head)
        return _h
