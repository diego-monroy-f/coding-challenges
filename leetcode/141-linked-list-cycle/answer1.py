# https://leetcode.com/problems/linked-list-cycle/
# Using Floyd's Turtle and Hare Algorithm -- own implementation (algorithm from course)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        tortoise = head
        hare = head
        while hare:
            tortoise = tortoise.next
            if hare.next:
                hare = hare.next.next
            else:
                return False
            if tortoise == hare:
                return True
                # This is only if we want to retrieve the node:
                # a = head
                # b = hare
                # while a != b:
                #     a = a.next
                #     b = b.next
        return False
