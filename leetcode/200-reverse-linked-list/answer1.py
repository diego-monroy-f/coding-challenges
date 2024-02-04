# https://leetcode.com/problems/reverse-linked-list/
# Brute-force solution -- own solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        new_head = None
        while current:
            new_head = ListNode(
                val=current.val,
                next=new_head
            )
            current = current.next
        return new_head
