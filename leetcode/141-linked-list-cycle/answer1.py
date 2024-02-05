# https://leetcode.com/problems/linked-list-cycle/
# Using Floyd's Turtle and Hare Algorithm -- own implementation (algorithm from course)
# FIXME: Why does this not work?!

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle = head
        hare = head
        while hare:
            tutle = turtle.next
            if hare.next:
                hare = hare.next.next
            else:
                return False
            if tutle == hare:
                return True
                # This is only if we want to retrieve the node:
                # a = head
                # b = hare
                # while a != b:
                #     a = a.next
                #     b = b.next
        return False
