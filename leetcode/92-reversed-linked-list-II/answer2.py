# https://leetcode.com/problems/reverse-linked-list-ii/
# Solution -- from course; same but looks better

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        current = head
        previous = head
        i = 1

        if head is None:
            return None

        while i < left:
            if i > 1:
                previous = previous.next
            current = current.next
            i += 1

        end = current
        new_head = None

        while left <= i <= right:
            _next = current.next
            current.next = new_head
            new_head = current
            current = _next
            i += 1

        previous.next = new_head
        end.next = current

        if left > 1:
            return head
        else:
            return new_head
