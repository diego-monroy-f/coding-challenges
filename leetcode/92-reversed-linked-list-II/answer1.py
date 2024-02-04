# https://leetcode.com/problems/reverse-linked-list-ii/
# Solution -- own

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
        end = None
        new_end = None
        while current:
            if i < left:
                if i > 1:
                    previous = previous.next
                current = current.next
                i += 1
            else:
                sub = current
                new_head = None
                while i <= right:
                    if i == right:
                        end = sub.next
                    if i == left:
                        new_end = sub
                    _next = sub.next
                    sub.next = new_head
                    new_head = sub
                    sub = _next
                    i += 1
                previous.next = new_head
                new_end.next = end
                if left == 1:
                    return new_head
                else:
                    return head
        return None
