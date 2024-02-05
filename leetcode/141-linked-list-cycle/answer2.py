# https://leetcode.com/problems/linked-list-cycle/
# Using Floyd's Turtle and Hare Algorithm -- course implementation

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        tortoise = head
        hare = head
        while True:
            tortoise = tortoise.next
            hare = hare.next
            if not hare or not hare.next:
                return False
            hare = hare.next
            if tortoise == hare:
                return True
